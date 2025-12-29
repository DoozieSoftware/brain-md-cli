# Contributing to Brain.md

Thank you for your interest in contributing to Brain.md! This guide will help you get started.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Welcome newcomers and help them learn
- Use clear and professional language

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip or pipenv for package management
- Git for version control

### Installation

```bash
# Clone the repository
git clone https://github.com/[username]/brain-md.git
cd brain-md

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

### Development Workflow

```bash
# 1. Create a feature branch
git checkout -b feature/your-feature-name

# 2. Make your changes
# ... write code ...

# 3. Run tests
pytest tests/

# 4. Commit your changes
git add .
git commit -m "feat: add your feature"

# 5. Push and create pull request
git push origin feature/your-feature-name
```

## Coding Standards

### Python Code Style

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and returns
- Write descriptive docstrings for all public functions
- Keep functions focused and single-purpose
- Maximum line length: 88 characters
- Use meaningful variable names

### Project-Specific Guidelines

- **TOON Format**: Always follow the spec in `spec/TOON_SPEC_v1.0.md`
- **Driver Prompts**: Use backticks (`>>>\``, ``<<<```) per `spec/DRIVER_PROMPT.md`
- **Error Messages**: Follow format from `design.md`

```python
# Good
def compile_brain(source: Path) -> CompileResult:
    """Compile brain.md into TOON payload."""
    pass

# Avoid
def compile(s):  # Too generic
    pass
```

### Import Order

1. Standard library imports
2. Third-party imports
3. Local imports

```python
import os
import re
from pathlib import Path
from rich.console import Console

from brain_md.models import CompileResult
from brain_md.compiler import compile_brain
```

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_compiler.py -v

# Run with coverage
pytest --cov=brain_md --cov-report=html

# Run specific property test (requires Hypothesis)
pytest tests/properties/test_compiler_properties.py::property1_valid_compilation_produces_output -v
```

### Test Coverage

We aim for 95% code coverage. CI will fail if coverage drops below 95%.

### Writing Tests

- **Unit Tests**: For specific functionality and edge cases
- **Property Tests**: For testing correctness properties with Hypothesis (100+ examples)
- **Integration Tests**: For testing complete workflows

Example property test:

```python
@given(content=valid_brain_content())
def property1_valid_compilation_produces_output(content: str):
    """
    Property 1: For any valid Brain_File, compiling it SHALL produce a non-empty Payload string.
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md') as f:
        f.write(content)
    
    result = compile_brain(Path(f.name))
    assert result.payload is not None
    assert len(result.payload) > 0
```

## Submitting Changes

### Pull Request Guidelines

1. **Descriptive Title**: Use conventional commits
   - `feat:` for new features
   - `fix:` for bug fixes
   - `refactor:` for code quality
   - `docs:` for documentation
   - `test:` for tests

2. **Clear Description**: Explain what and why
   - What problem does this solve?
   - How does it solve it?
   - Are there any trade-offs?
   - Include test results

3. **Tests**: All tests must pass
   - Run full test suite before creating PR
   - Include test coverage percentage

4. **Documentation**: Update relevant docs if needed
   - Update CHANGELOG.md
   - Update README.md if user-facing changes

### Commit Message Format

```
<type>[<scope>]: <subject>

<body>

<footer>

Refs #<issue-number>
```

Example:

```
feat(watcher): add file debouncing to watch mode

Implemented 0.5s debounce to prevent rapid recompiles
when multiple files change simultaneously. This reduces CPU usage
and prevents duplicate notifications.

- Added debounce parameter to BrainFileHandler
- Modified trigger_callback_if_pending() to check elapsed time
- Added tests for debounce functionality
- Updated documentation

Fixes #123
```

## Release Process

1. Update version in `brain_md/__init__.py`
2. Update CHANGELOG.md with release notes
3. Create git tag: `git tag v0.x.0`
4. Create GitHub release
5. Upload to PyPI (for maintainers)

## Questions?

- Check existing [Issues](https://github.com/[username]/brain-md/issues)
- Check [Discussions](https://github.com/[username]/brain-md/discussions)
- Ask in your PR if you need guidance

Thanks for contributing to Brain.md!
