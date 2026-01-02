# SegTrace
SegTrace is a web-based debugging assistant for C/C++ programs. It automatically compiles and runs user-submitted code, 
detects runtime failures, captures execution evidence using GDB, and generates plain-language explanations of crashes 
grounded in real debugger output. Unlike generic AI code assistants, SegTrace focuses on post-failure diagnosis: it 
explains why a program crashed at a specific point in execution and what concrete changes would fix it based on runtime 
traces rather than speculation.

## Features
- Automatic compilation and execution of C/C++ programs
- Runtime crash detection (e.g. segmentation faults, aborts)
- GDB-driven crash analysis (signal, faulting function, line, backtrace)
- Web interface with file upload and paste-in code input

## Goals
- Automate GDB-based debugging
- Explain runtime crashes (e.g. segfaults)
- Compare program behavior before and after fixes
- Identify the precise fault location and invalid state

## Architecture Overview
- Compile user code using GCC
- Run the binary and detect crashes
- Invoke GDB to capture backtraces and faulting context
- Analyze debugger output into structured data
- Generate explanations using a local instruction-tuned LLM (In Progress...)
- Present results via a web interface

## Tech Stack
- Backend: Python, FastAPI
- Debugging: GDB
- Compilation: GCC / Clang
- Frontend: Jinja2 templates
- AI: In Progress...

## Status
In Progress...
Core backend pipeline (compile → run → debug → analyze → explain) is implemented.
Frontend and explanation quality are actively being refined.
