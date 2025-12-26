# SegTrace
SegTrace is a web-based debugging assistant for C/C++ programs.
It automatically compiles and runs user code, captures runtime failures
using GDB, and explains crashes in plain language using execution evidence.
It focuses on post-failure diagnosis by combining runtime traces, debugger 
output, and structured reasoning.

## Goals
- Automate GDB-based debugging
- Explain runtime crashes (e.g. segfaults)
- Compare program behavior before and after fixes
- Support interview-style debugging workflows

## Tech Stack
- Python
- GDB
- GCC / Clang
- Django + Jinja2
- LLM API (Azure / AWS)

## Status
In Progress...
