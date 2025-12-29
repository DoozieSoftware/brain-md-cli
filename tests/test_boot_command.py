"""Tests for the boot command."""

import pytest
import tempfile
from pathlib import Path
from brain_md.boot import boot_cmd, _generate_context_content


def test_boot_creates_context_file():
    """Test that boot command creates context.md from brain.md."""
    # Create a temporary brain.md
    brain_content = """
# brain.md

KERNEL:
  role: "Developer"
  mode: "Strict/Code-Only"

REGISTERS:
  project: "test-project"

MEMORY_POINTERS[1]{type, path}:
  file, "@test.md"

PROCESS_STACK[1]{priority, task}:
  1, "Test task"
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        brain_path = Path(tmpdir) / "brain.md"
        brain_path.write_text(brain_content)

        # Create test.md (referenced by pointer)
        test_file = Path(tmpdir) / "test.md"
        test_file.write_text("Test content")

        # Run boot command
        boot_cmd(brain_path)

        # Verify context.md was created
        context_path = Path(tmpdir) / "context.md"
        assert context_path.exists()

        # Verify content structure
        context = context_path.read_text()
        assert "# context.md - Live Session State" in context
        assert "KERNEL:" in context
        assert "REGISTERS:" in context
        assert "MEMORY_POINTERS[" in context
        assert "PROCESS_STACK[" in context
        assert "SESSION_SCRATCHPAD:" in context
        assert 'role: "Developer"' in context
        assert 'project: "test-project"' in context


def test_generate_context_content():
    """Test that context content is generated correctly."""
    source = """
KERNEL:
  role: "Test"

REGISTERS:
  key: "value"
"""

    result = _generate_context_content(source)

    assert "# context.md - Live Session State" in result
    assert "KERNEL:" in result
    assert "REGISTERS:" in result
    assert "SESSION_SCRATCHPAD:" in result
    assert 'role: "Test"' in result
    assert 'key: "value"' in result
    assert "session_notes" in result
    assert "todo_list" in result
    assert "current_focus" in result


def test_boot_with_pointers():
    """Test that boot handles memory pointers correctly."""
    brain_content = """
KERNEL:
  role: "Developer"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@agents.md", "Agent definitions"
  file, "@schema.sql", "Database schema"
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        brain_path = Path(tmpdir) / "brain.md"
        brain_path.write_text(brain_content)

        # Create referenced files
        (Path(tmpdir) / "agents.md").write_text("Agents content")
        (Path(tmpdir) / "schema.sql").write_text("CREATE TABLE test (id INT);")

        # Run boot command
        boot_cmd(brain_path)

        # Verify context.md
        context_path = Path(tmpdir) / "context.md"
        context = context_path.read_text()

        # Pointers should have @ prefix
        assert '"@agents.md"' in context
        assert '"@schema.sql"' in context


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
