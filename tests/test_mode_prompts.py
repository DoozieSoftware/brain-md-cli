"""Tests for mode-specific driver prompts."""

import pytest
from pathlib import Path
import tempfile
import textwrap
from brain_md.compiler import compile_brain


def test_strict_mode_prompt():
    """Test that strict mode generates correct driver prompt."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
          mode: "Strict/Code-Only"
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Should contain strict mode prompt
        assert "STRICT MODE: Code only, no explanations" in result.payload
        # Driver prompt should be at the start
        lines = result.payload.split("\n")
        assert lines[0].startswith("SYSTEM RESET")
    finally:
        temp_path.unlink()


def test_creative_mode_prompt():
    """Test that creative mode generates correct driver prompt."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
          mode: "Creative"
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Should contain creative mode prompt
        assert "CREATIVE MODE: Explore freely within constraints" in result.payload
        # Driver prompt should be at the start
        lines = result.payload.split("\n")
        assert lines[0].startswith("SYSTEM RESET")
    finally:
        temp_path.unlink()


def test_analysis_mode_prompt():
    """Test that analysis mode generates correct driver prompt."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
          mode: "Analysis"
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Should contain analysis mode prompt
        assert "ANALYSIS MODE: Review and report, no modifications" in result.payload
        # Driver prompt should be at the start
        lines = result.payload.split("\n")
        assert lines[0].startswith("SYSTEM RESET")
    finally:
        temp_path.unlink()


def test_default_mode_prompt():
    """Test that default mode generates standard driver prompt."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
          mode: "some-other-mode"
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Should contain standard prompt (not mode-specific)
        assert "``` denotes raw file content. EXECUTE `PROCESS_STACK`" in result.payload
        assert "STRICT MODE" not in result.payload
        assert "CREATIVE MODE" not in result.payload
        assert "ANALYSIS MODE" not in result.payload
        # Driver prompt should be at the start
        lines = result.payload.split("\n")
        assert lines[0].startswith("SYSTEM RESET")
    finally:
        temp_path.unlink()


def test_no_mode_prompt():
    """Test that no mode specified uses standard driver prompt."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)

        # Should contain standard prompt
        assert "``` denotes raw file content. EXECUTE `PROCESS_STACK`" in result.payload
        # Driver prompt should be at the start
        lines = result.payload.split("\n")
        assert lines[0].startswith("SYSTEM RESET")
    finally:
        temp_path.unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
