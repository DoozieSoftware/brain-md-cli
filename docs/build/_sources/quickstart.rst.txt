Quick Start Guide
=================

This guide will help you get started with Brain.md in just a few minutes.

Basic Workflow
--------------

1. **Create a brain.md file**

   .. code-block:: yaml

       KERNEL:
         role: "Senior Developer"
         mode: "Strict/Code-Only"
         token_budget: 4000

       REGISTERS:
         project: "my-app"

       MEMORY_POINTERS[1]{type, path, description}:
         file, "@schema.sql", "Database schema"

       PROCESS_STACK[1]{priority, task}:
         1, "Optimize queries"

2. **Create referenced files**

   .. code-block:: sql

       CREATE TABLE users (
           id INT PRIMARY KEY,
           name TEXT NOT NULL
       );

3. **Boot a session**

   .. code-block:: bash

       brain boot brain.md

   This creates a ``context.md`` file with all sections plus a new ``SESSION_SCRATCHPAD`` for live editing.

4. **Watch for changes**

   .. code-block:: bash

       brain watch context.md

   Any changes to ``context.md`` or referenced files will trigger automatic recompilation and copy to clipboard.

Example Session
---------------

.. code-block:: bash

   # Step 1: Create your brain.md
   cat > brain.md <<'EOF'
   KERNEL:
     role: "Full-Stack Developer"
     mode: "Creative"

   REGISTERS:
     project: "todo-app"

   MEMORY_POINTERS[1]{type, path, description}:
     file, "@main.py", "Main application"

   PROCESS_STACK[2]{priority, task}:
     1, "Add authentication"
     2, "Implement pagination"
   EOF'

   # Step 2: Boot session
   brain boot brain.md
   # Output: ✔ Session boot successful...

   # Step 3: Edit context.md SESSION_SCRATCHPAD
   # Add your session notes, todos, and current focus

   # Step 4: Watch for changes
   brain watch context.md
   # Any edits trigger auto-recompile to clipboard

   # Step 5: Paste clipboard into your LLM interface
   # The AI receives the complete TOON payload

Tips for Effective Use
---------------------

* **Use the SESSION_SCRATCHPAD**: This is your live RAM - add notes, todos, and current focus during sessions
* **Keep brain.md as source of truth**: Make permanent changes in brain.md, temporary changes in context.md
* **Use watch mode**: Let the tool handle recompilation automatically
* **Leverage pointers**: Reference external files instead of copying content directly
* **Set token budgets**: Prevent context overflow by setting appropriate budgets in KERNEL

Next Steps
----------

* :doc:`commands` - Learn about all CLI commands
* :doc:`toon_format` - Understand the TOON format specification
* :doc:`advanced_usage` - Explore advanced features and patterns
