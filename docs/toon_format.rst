TOON Format
============

TOON (Token-Oriented Object Notation) is a text format optimized for minimal token usage while maintaining human readability.

Sections
----------

TOON uses uppercase headers followed by a colon to define sections.

.. code-block:: yaml

   KERNEL:
   REGISTERS:
   MEMORY_POINTERS:
   PROCESS_STACK:
   SESSION_SCRATCHPAD:

Key-Value Pairs
----------------

Indented under headers with two-space indent.

.. code-block:: yaml

   KERNEL:
     role: "Senior Developer"
     mode: "Strict/Code-Only"
     token_budget: 4000

Tabular Arrays
--------------

High-density lists that define keys once to save tokens.

**Format**: ``SECTION_NAME[count]{key1, key2, ...}:``

.. code-block:: yaml

   MEMORY_POINTERS[2]{type, path, description}:
     file, "@schema.sql", "Database schema"
     file, "@api.py", "API endpoints"

Equivalent JSON:

.. code-block:: json

   {
     "MEMORY_POINTERS": [
       {"type": "file", "path": "@schema.sql", "description": "Database schema"},
       {"type": "file", "path": "@api.py", "description": "API endpoints"}
     ]
   }

Pointers
---------

Strings prefixed with ``@`` reference external files.

.. code-block:: yaml

   MEMORY_POINTERS[1]{type, path}:
     file, "@config.py"

With line ranges:

.. code-block:: yaml

   MEMORY_POINTERS[1]{type, path}:
     file, "@app.py:10-50"

This injects only lines 10-50 from ``app.py`` into the compiled payload.

Heredocs
---------

Raw text blocks delimited by ``>>>`` and ``<<<``. No escaping required.

.. code-block:: yaml

   MEMORY_POINTERS[1]{type, path, description}:
     file, "@query.sql", "SQL query"

**query.sql**:

.. code-block:: sql

   >>>
   SELECT users.name, orders.total
   FROM users
   JOIN orders ON users.id = orders.user_id
   <<<

Heredocs are preserved as-is in the final payload.

Comments
---------

Lines starting with ``#`` are comments and are stripped from final compiled payload, but preserved in source file for editing.

.. code-block:: yaml

   # This is a comment and will be stripped from compiled output
   KERNEL:
     role: "Developer"

Reserved Sections
-----------------

| Section | Purpose |
|---------|---------|
| ``KERNEL:`` | Core AI configuration (role, mode, constraints) |
| ``REGISTERS:`` | Session variables (paths, phase, state) |
| ``MEMORY_POINTERS:`` | External file references |
| ``PROCESS_STACK:`` | Prioritized task queue |
| ``SESSION_SCRATCHPAD:`` | Live session notes (created by boot) |
| ``RESOLVED_MEMORY:`` | Compiler-generated section with injected file contents |

Indentation
------------

* Two spaces per level (no tabs)
* Tabular array rows are indented once under the header
* Heredoc content is NOT indented

String Values
-------------

* Quoted strings: ``"value with spaces"``
* Unquoted allowed for single words: ``mode: strict``
* Pointers must be quoted: ``"@file.md"``

Complete Example
---------------

.. code-block:: yaml

   # brain.md (TOON Format)

   KERNEL:
     role: "Senior Architect"
     mode: "Strict/Code-Only"
     token_budget: 4000

   REGISTERS:
     project_root: "./src"
     current_phase: "Migration"

   MEMORY_POINTERS[2]{type, path, description}:
     file, "@agents.md", "Team Persona Definitions"
     file, "@schema.sql", "Database Structure"

   PROCESS_STACK[3]{priority, task}:
     1, "Analyze Schema for Indexing"
     2, "Draft Migration Script"
     3, "Update Documentation"

For the complete TOON specification, see :doc:`../spec/TOON_SPEC_v1_0`.
