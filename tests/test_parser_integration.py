"""Basic tests for parser integration with compiler."""

import pytest
from pathlib import Path
from brain_md.compiler import compile_brain
from brain_md.models import CompileResult


def test_parser_integration_basic():
    """Test that compiler uses parser and returns CompileResult."""
    source = Path("examples/brain.md")

    if not source.exists():
        pytest.skip("Example file not found")

    result = compile_brain(source)

    # Verify return type is CompileResult
    assert isinstance(result, CompileResult)

    # Verify payload is non-empty
    assert len(result.payload) > 0

    # Verify payload starts with driver prompt
    assert result.payload.startswith("SYSTEM RESET")

    # Verify token count is positive
    assert result.token_count > 0

    # Verify resolved_pointers is a list
    assert isinstance(result.resolved_pointers, list)


def test_parser_has_brain_config():
    """Test that parsed content has BrainConfig structure."""
    from brain_md.parser import parse_toon

    content = """
KERNEL:
  role: "Test"
  mode: "strict"

REGISTERS:
  key: "value"
"""

    parsed = parse_toon(content)

    # Verify KERNEL section exists
    assert "KERNEL" in parsed
    assert parsed["KERNEL"]["role"] == "Test"
    assert parsed["KERNEL"]["mode"] == "strict"

    # Verify REGISTERS section exists
    assert "REGISTERS" in parsed
    assert parsed["REGISTERS"]["key"] == "value"


def test_compiler_with_token_budget():
    """Test that compiler extracts token_budget from KERNEL."""
    from brain_md.compiler import compile_brain
    from pathlib import Path
    import tempfile
    import textwrap

    # Create temporary brain.md with token budget
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
          token_budget: 4000
        
        MEMORY_POINTERS[0]{type, path, description}:
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Verify token_budget is extracted
        assert result.token_budget == 4000
    finally:
        temp_path.unlink()


def test_compiler_resolves_pointers():
    """Test that compiler resolves pointers and tracks them."""
    from brain_md.compiler import compile_brain
    from pathlib import Path
    import tempfile
    import textwrap

    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        brain_file = Path(tmpdir) / "brain.md"
        ref_file = Path(tmpdir) / "ref.txt"

        ref_file.write_text("Referenced content")

        content = textwrap.dedent(f"""
            KERNEL:
              role: "Test"
            
            MEMORY_POINTERS[1]{{type, path, description}}:
              file, "@ref.txt", "Reference file"
            """)

        brain_file.write_text(content)

        result = compile_brain(brain_file)

        # Verify pointer was resolved
        assert len(result.resolved_pointers) == 1
        assert result.resolved_pointers[0].content == "Referenced content"
        assert "@ref.txt:" in result.payload


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
