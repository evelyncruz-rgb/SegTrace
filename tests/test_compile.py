from app.compiler.gcc import compile_c

if __name__ == "__main__":
    res = compile_c("tests/segfault.c", "sandbox/a.out")
    print(res)