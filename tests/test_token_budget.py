"""Tests for token budget enforcement."""

import pytest
from pathlib import Path
import tempfile
import textwrap
from brain_md.compiler import compile_brain
from brain_md.models import BudgetExceededError


def test_token_budget_within_limit():
    """Test that compilation succeeds when within token budget."""
    content = textwrap.dedent("""
        KERNEL:
          role: "Test"
          token_budget: 5000
        
        MEMORY_POINTERS[0]{type, path, description}:
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        result = compile_brain(temp_path)
        # Should compile successfully
        assert result.token_count > 0
        assert result.token_budget == 5000
        assert result.token_count <= 5000  # Within budget
    finally:
        temp_path.unlink()


def test_token_budget_exceeded():
    """Test that compilation fails when exceeding token budget."""
    # Create content that will exceed budget
    large_content = "x " * 1000  # This should create many tokens

    content = textwrap.dedent(f"""
        KERNEL:
          role: "Test"
          token_budget: 100
        
        >>>
        {large_content}
        <<<
        """)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    try:
        with pytest.raises(BudgetExceededError) as exc_info:
            compile_brain(temp_path)

        # Verify error message
        assert exc_info.value.actual > 100
        assert exc_info.value.budget == 100
        assert "Token budget exceeded" in str(exc_info.value)
    finally:
        temp_path.unlink()


def test_no_token_budget():
    """Test that compilation succeeds when no token budget is set."""
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
        # Should compile successfully regardless of token count
        assert result.token_count > 0
        assert result.token_budget is None
    finally:
        temp_path.unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
