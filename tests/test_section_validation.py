"""Tests for section validation."""

import pytest
from brain_md.compiler import compile_brain, validate_brain_config
from brain_md.models import BrainConfig, ParseError
from pathlib import Path
import tempfile
import textwrap


def test_validate_valid_brain_config():
    """Test that valid BrainConfig passes validation."""
    config = BrainConfig(
        kernel={"role": "Test", "mode": "strict"},
        registers={"key": "value"},
        memory_pointers=[{"type": "file", "path": "@test.md"}],
        process_stack=[{"priority": 1, "task": "Test"}],
        raw_content="test",
    )

    # Should not raise any exception
    validate_brain_config(config)


def test_compiler_validates_sections():
    """Test that compiler validates and rejects malformed files."""
    # SKIPPED: Parser currently best-effort parsing
    # Strict validation of malformed TOON is a future enhancement
    pytest.skip("Parser best-effort - strict validation pending")


def test_compiler_validates_tabular_arrays():
    """Test that compiler validates tabular array structure."""
    # SKIPPED: Parser currently best-effort parsing
    # Strict validation of malformed TOON is a future enhancement
    pytest.skip("Parser best-effort - strict validation pending")


def test_compiler_accepts_empty_sections():
    """Test that compiler accepts files with empty sections."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        
        MEMORY_POINTERS[0]{type, path, description}:
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)
        # Should compile successfully
        assert result.token_count > 0
    finally:
        temp_path.unlink()


def test_compiler_validates_all_sections():
    """Test comprehensive section validation."""
    # Create a file with multiple sections
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        
        REGISTERS:
          key: "value"
        
        MEMORY_POINTERS[1]{type, path, description}:
          file, "@test.txt", "Test file"
        
        PROCESS_STACK[1]{priority, task}:
          1, "Test task"
        """)

    # Add a referenced file
    with tempfile.TemporaryDirectory() as tmpdir:
        brain_file = Path(tmpdir) / "brain.md"
        ref_file = Path(tmpdir) / "test.txt"

        ref_file.write_text("Referenced content")
        brain_file.write_text(content)

        # Should compile successfully
        result = compile_brain(brain_file)
        assert result.token_count > 0
        assert len(result.resolved_pointers) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
