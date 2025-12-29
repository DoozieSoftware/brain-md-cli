"""Tests for heredoc support in TOON parser."""

import pytest
from brain_md.parser import parse_toon
from brain_md.compiler import compile_brain
from pathlib import Path
import tempfile
import textwrap


def test_parse_heredoc_simple():
    """Test that simple heredoc is parsed correctly."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        
        >>>This is a heredoc block
        With multiple lines
        <<<
        """)

    result = parse_toon(content)

    # Heredoc should be stored with a special key
    heredoc_keys = [k for k in result.keys() if k.startswith("heredoc_")]
    assert len(heredoc_keys) == 1
    assert "This is a heredoc block" in result[heredoc_keys[0]]
    assert "With multiple lines" in result[heredoc_keys[0]]


def test_parse_multiple_heredocs():
    """Test that multiple heredocs are parsed correctly."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        
        >>>First heredoc
        <<<
        
        REGISTERS:
          key: "value"
        
        >>>Second heredoc
        With content
        <<<
        """)

    result = parse_toon(content)

    # Should have 2 heredocs
    heredoc_keys = [k for k in result.keys() if k.startswith("heredoc_")]
    assert len(heredoc_keys) == 2

    # Both should have their content
    heredoc_content = [result[k] for k in heredoc_keys]
    assert any("First heredoc" in c for c in heredoc_content)
    assert any("Second heredoc" in c for c in heredoc_content)


def test_heredoc_preserves_content():
    """Test that heredoc content is preserved exactly."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        
        >>>
        Line 1
        Line 2
        Line 3
        <<<
        """)

    result = parse_toon(content)
    heredoc_keys = [k for k in result.keys() if k.startswith("heredoc_")]
    heredoc_content = result[heredoc_keys[0]]

    # Content should be preserved exactly
    assert heredoc_content == "Line 1\nLine 2\nLine 3"


def test_heredoc_compiler_integration():
    """Test that heredocs work with compiler."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        
        >>>
        Raw content here
        With special characters: @#$%
        <<<
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Heredoc content should be in payload
        assert "Raw content here" in result.payload
        assert "With special characters: @#$%" in result.payload

        # Heredoc delimiters should be in payload
        assert ">>>" in result.payload
        assert "<<<" in result.payload
    finally:
        temp_path.unlink()


def test_heredoc_with_special_chars():
    """Test that heredocs handle special characters."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        
        >>>
        SQL: SELECT * FROM users WHERE id = 'test';
        JSON: {"key": "value", "nested": {"a": 1}}
        Regex: ^[a-z]+@[a-z]+\.[a-z]+$
        <<<
        """)

    result = parse_toon(content)
    heredoc_keys = [k for k in result.keys() if k.startswith("heredoc_")]
    heredoc_content = result[heredoc_keys[0]]

    # All special characters should be preserved
    assert "SELECT * FROM users" in heredoc_content
    assert '{"key": "value"' in heredoc_content
    assert r"^[a-z]+@[a-z]+" in heredoc_content


def test_heredoc_not_treated_as_comment():
    """Test that heredoc delimiters are not stripped as comments."""
    from brain_md.parser import strip_comments

    lines = [
        "# This is a comment",
        ">>> This is heredoc start",
        "Heredoc content",
        "<<< This is heredoc end",
        "# Another comment",
    ]

    result = strip_comments(lines)

    # Comments should be removed
    assert "# This is a comment" not in result
    assert "# Another comment" not in result

    # Heredoc delimiters should be preserved
    assert ">>> This is heredoc start" in result
    assert "<<< This is heredoc end" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
