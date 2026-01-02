from app.compiler.gcc import compile_c
from app.debugger.gdb import run_gdb
if __name__ == "__main__":
    # Compile the segfault program first
    compile_c("tests/segfault.c", "sandbox/a.out")

    # Run gdb on the binary
    gdb_res = run_gdb("sandbox/a.out")
    print("GDB STDOUT:\n", gdb_res["stdout"])
    print("GDB STDERR:\n", gdb_res["stderr"])
    