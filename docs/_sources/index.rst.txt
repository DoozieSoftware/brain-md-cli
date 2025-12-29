.. Brain.md documentation master file

Brain.md - Context Control Protocol for LLMs
==========================================

Brain.md is a CLI tool that compiles human-readable ``brain.md`` files into token-optimized TOON (Token-Oriented Object Notation) payloads for injection into Large Language Model (LLM) context windows.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   commands
   toon_format
   advanced_usage

Features
--------

* **TOON Parser**: Full-featured parser supporting sections, key-value pairs, tabular arrays, and heredocs
* **Pointer Resolution**: Automatically resolves and injects external file references
* **Live Context Management**: ``brain boot`` creates editable context.md for session state
* **Watch Mode**: Auto-recompiles on file changes with debouncing and OS notifications
* **Token Budget Enforcement**: Ensures payloads stay within specified token limits
* **Mode-Specific Prompts**: Supports Strict, Creative, and Analysis driver prompt modes
* **Comment Stripping**: Removes comments from final payload while preserving in source files

Installation
------------

.. code-block:: bash

   pip install -e ".[dev]"

Quick Start
-----------

.. code-block:: bash

   # Create a brain.md file
   cat > brain.md <<'EOF'
   KERNEL:
     role: "Senior Developer"
     mode: "Strict/Code-Only"
     token_budget: 4000

   MEMORY_POINTERS[1]{type, path, description}:
     file, "@schema.sql", "Database schema"
   EOF'

   # Boot a session (creates context.md with SESSION_SCRATCHPAD)
   brain boot brain.md

   # Watch for changes
   brain watch context.md

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

API Reference
=============

.. automodule:: brain_md
   :members:

.. automodule:: brain_md.compiler
   :members:

.. automodule:: brain_md.parser
   :members:

.. automodule:: brain_md.pointer
   :members:

.. automodule:: brain_md.watcher
   :members:

.. automodule:: brain_md.boot
   :members:

.. automodule:: brain_md.models
   :members:
