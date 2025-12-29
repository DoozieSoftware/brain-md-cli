CLI Commands
=============

This page documents all available CLI commands in Brain.md.

brain boot
----------

Initialize a session by creating ``context.md`` from ``brain.md``.

**Usage**::

   brain boot <source>

**Description**:

The ``boot`` command creates a live, editable ``context.md`` file from your source ``brain.md``. This is your working RAM during a session.

**Features**:

* Creates live, editable context.md file
* Preserves all TOON sections (KERNEL, REGISTERS, MEMORY_POINTERS, PROCESS_STACK)
* Adds SESSION_SCRATCHPAD for live session notes
* Generates session metadata (timestamp, source file)
* Verifies compilation success

**Example**::

   brain boot brain.md

**Output**::

   ✔ Session boot successful
      Source: brain.md
      Context: context.md
      Tokens: 360
      Pointers Resolved: 2

   💡 Tip: Run 'brain watch' to monitor context.md for live compilation

**context.md Structure**:

.. code-block:: yaml

   # context.md - Live Session State
   # Generated from brain.md by 'brain boot' command

   # === KERNEL (AI Configuration) ===
   KERNEL:
     role: "Senior Developer"
     mode: "Strict/Code-Only"

   # === REGISTERS (Session Variables) ===
   REGISTERS:
     project: "my-project"

   # === MEMORY_POINTERS (External References) ===
   MEMORY_POINTERS[1]{type, path}:
     file, "@schema.sql"

   # === PROCESS_STACK (Task Queue) ===
   PROCESS_STACK[1]{priority, task}:
     1, "Initial task"

   # === SESSION_SCRATCHPAD (Live Notes) ===
   SESSION_SCRATCHPAD:
     session_notes: >-
       Add your session notes here...

     todo_list:
       - "First thing to do"

     current_focus: >-
       What you're working on right now...

brain compile
-------------

Compiles a brain.md or context.md file into a token-optimized TOON payload.

**Usage**::

   brain compile <source> [OPTIONS]

**Options**:

``--clipboard, -c``
   Copy output to system clipboard

``--output, -o <path>``
   Write output to file instead of stdout

**Examples**::

   # Compile to stdout
   brain compile brain.md

   # Compile to clipboard
   brain compile brain.md --clipboard

   # Compile to file
   brain compile brain.md --output context.toon

   # Compile context.md
   brain compile context.md --clipboard

brain watch
------------

Watches brain.md or context.md and all referenced ``@pointer`` files for changes, auto-recompiling.

**Usage**::

   brain watch <source>

**Features**:

* Monitors source file and all referenced files
* Auto-recompiles on any file change
* Copies to clipboard on recompile
* Sends OS notifications for success/failure
* 0.5s debounce to prevent rapid recompiles
* Press Ctrl+C to stop watching

**Example**::

   brain watch context.md

**Output**::

   👀 Watching context.md...
   Press Ctrl+C to stop

   ✔ Brain.md compiled: 360 tokens, 2 files resolved

brain flush
------------

*(Coming in v0.4.0)*

Flush context stack - mark tasks/notes/registers as complete.

**Usage**::

   brain flush <source> [OPTIONS]

**Options**:

``--pointers, -p``
   Clear all pointer contexts (LIFO order)

``--notes, -n``
   Clear all note entries

``--registers, -r``
   Clear all registers

``--all, -a``
   Flush everything (stack + all entries)

``--force, -f``
   Force flush even if stack is empty
