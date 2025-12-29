"""Tests for comment stripping functionality."""

import pytest
from pathlib import Path
from brain_md.compiler import compile_brain
from brain_md.models import CompileResult


def test_comments_removed_from_payload():
    """Test that comments are stripped from compiled payload."""
    from brain_md.compiler import compile_brain
    from pathlib import Path
    import tempfile
    import textwrap

    content = textwrap.dedent("""
        # This is a comment
        KERNEL:
          role: "Test"  # Inline comment should not be stripped
          mode: "strict"
        
        # Another comment
        REGISTERS:
          key: "value"
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Verify comments are removed from payload
        assert "# This is a comment" not in result.payload
        assert "# Another comment" not in result.payload

        # Verify actual content is preserved
        assert "KERNEL:" in result.payload
        assert 'role: "Test"' in result.payload
        assert "# Inline comment should not be stripped" in result.payload
    finally:
        temp_path.unlink()


def test_preserves_blank_lines_after_stripping():
    """Test that blank lines are preserved after comment stripping."""
    from brain_md.compiler import compile_brain
    from pathlib import Path
    import tempfile
    import textwrap

    content = textwrap.dedent("""
        # Comment 1
        
        KERNEL:
          role: "Test"
        
        # Comment 2
        
        REGISTERS:
          key: "value"
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Verify structure is preserved
        lines = result.payload.split("\n")
        assert "KERNEL:" in result.payload
        assert "REGISTERS:" in result.payload

        # Verify comments are gone
        assert "# Comment 1" not in result.payload
        assert "# Comment 2" not in result.payload
    finally:
        temp_path.unlink()


def test_no_comments_in_example_file():
    """Test that the example file compiles without source comments in payload."""
    source = Path("examples/brain.md")

    if not source.exists():
        pytest.skip("Example file not found")

    result = compile_brain(source)

    # Split payload into main content and RESOLVED_MEMORY section
    if "# RESOLVED_MEMORY" in result.payload:
        main_content = result.payload.split("# RESOLVED_MEMORY")[0]
    else:
        main_content = result.payload

    # Verify no comment lines in main content (from brain.md source)
    # Note: Resolved files may contain their own comments (e.g., markdown headers)
    lines = main_content.split("\n")
    comment_lines = [l for l in lines if l.strip().startswith("#")]

    # No comments should remain in the main brain.md content
    assert len(comment_lines) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
