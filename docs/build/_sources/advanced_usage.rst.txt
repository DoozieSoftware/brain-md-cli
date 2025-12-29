Advanced Usage
==============

This page covers advanced features and patterns for Brain.md.

Token Budget Enforcement
-----------------------

Enforce a maximum token count for compiled payload.

.. code-block:: yaml

   KERNEL:
     role: "Developer"
     token_budget: 1000

If compiled payload exceeds token budget, compilation will fail with a ``BudgetExceededError``.

**Example output**::

   ✗ Compilation failed: Token budget exceeded: 1500 tokens (budget: 1000)

Mode-Specific Driver Prompts
-----------------------------

Brain.md automatically generates mode-specific driver prompts based on ``mode`` value in the KERNEL section.

| Mode | Driver Prompt |
|------|---------------|
| ``strict`` or ``code-only`` | ``SYSTEM RESET. FORMAT=TOON. STRICT MODE: Code only, no explanations. \`>>>` denotes raw file. EXECUTE \`PROCESS_STACK\`.`` |
| ``creative`` | ``SYSTEM RESET. FORMAT=TOON. CREATIVE MODE: Explore freely within constraints. \`>>>` denotes raw file. EXECUTE \`PROCESS_STACK\`.`` |
| ``analysis`` or ``planning`` | ``SYSTEM RESET. FORMAT=TOON. ANALYSIS MODE: Review and report, no modifications. \`>>>` denotes raw file. EXECUTE \`PROCESS_STACK\`.`` |
| Other (default) | ``SYSTEM RESET. FORMAT=TOON. \`>>>` denotes raw file content. EXECUTE \`PROCESS_STACK\`.`` |

**Example**:

.. code-block:: yaml

   KERNEL:
     role: "Developer"
     mode: "Strict/Code-Only"

   # Generates strict mode driver prompt
   # SYSTEM RESET. FORMAT=TOON. STRICT MODE: Code only, no explanations...

Multiple Pointers with Line Ranges
----------------------------------

Combine multiple file references with selective line ranges.

.. code-block:: yaml

   MEMORY_POINTERS[3]{type, path, description}:
     file, "@schema.sql:1-100", "Schema definition"
     file, "@main.py:50-100", "Main function"
     file, "@utils.py:1-50", "Utility functions"

This injects only the specified line ranges, saving tokens.

State Management vs Chat History
------------------------------

**Key Concept**: Brain.md manages **live state**, not chat history.

* **Live State (RAM)**: The current configuration of ``context.md``
* **Not History**: We don't log user prompts or AI replies
* **Session**: Defined by the current state of the file, not timeline

**Best Practices**:

* Use ``SESSION_SCRATCHPAD`` for session notes (temporary)
* Use ``brain.md`` for permanent configurations
* Reboot session with ``brain boot`` when needed
* Don't track chat history in files (violates "Flush" principle)

Watch Mode with Dynamic Pointers
--------------------------------

The watcher automatically detects new pointer references.

.. code-block:: bash

   brain watch context.md

When you add a new pointer to ``context.md``:

1. Watcher detects the change
2. Recompiles automatically
3. Adds new file to watch list
4. Copies payload to clipboard

Debouncing prevents rapid recompiles (0.5s default).

Using Heredocs for Source Code
------------------------------

Embed source code directly using heredocs.

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
   -- Runs the query and joins users with orders

Heredocs preserve all formatting, including:

* SQL queries
* Code snippets
* Configuration blocks
* Any raw text content

Comment Stripping Strategy
-------------------------

Comments (lines starting with ``#``) are stripped from final payload but preserved in source files.

**Source (brain.md)**:

.. code-block:: yaml

   # This explains the kernel configuration
   KERNEL:
     role: "Developer"

   REGISTERS:
     # Project root directory
     project: "./src"

**Compiled Payload**:

.. code-block:: text

   KERNEL:
     role: "Developer"

   REGISTERS:
     project: "./src"

This keeps your source files readable while minimizing tokens.

Debugging Compilation
--------------------

Enable verbose output to debug pointer resolution and token counting.

.. code-block:: bash

   # Compile with output to see what's being generated
   brain compile brain.md

   # Check token count
   brain compile brain.md

   Output:
   SYSTEM RESET. FORMAT=TOON...
   ...
   (360 tokens, 2 files resolved)

If pointers fail to resolve:

.. code-block:: text

   ✗ Compilation failed: Pointer target not found: @missing.md -> /path/to/file

Ensure the file exists relative to the source file.

Integration with LLMs
---------------------

**Workflow**:

1. Create ``brain.md`` with your context
2. Boot session: ``brain boot brain.md``
3. Watch for changes: ``brain watch context.md``
4. Edit ``context.md`` during your session
5. Copy compiled payload from clipboard
6. Paste into LLM interface

**Benefits**:

* Minimal token usage (TOON format)
* Live editing with auto-recompile
* Clean separation of concerns
* No chat history bloat

Next Steps
----------

* :doc:`../spec/TOON_SPEC_v1_0` - Complete TOON format specification
* :doc:`../spec/DRIVER_PROMPT` - Driver prompt specification
