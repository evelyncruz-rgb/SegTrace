from app.compiler.gcc import compile_c
from app.debugger.runner import run
from app.debugger.gdb import run_gdb
from app.debugger.analyzer import analyze
from app.llm.explainer import explain_crash

def run_pipeline(source_file: str, source_code: str | None = None):
    compile_res = compile_c(source_file, "sandbox/a.out")
    if not compile_res["success"]:
        return compile_res

    run_res = run("sandbox/a.out")
    if not run_res["crashed"]:
        return {"status": "no crash"}

    gdb_res = run_gdb("sandbox/a.out")
    analysis = analyze(gdb_res)

    explanation = explain_crash(analysis, source_code)

    return {
        "analysis": analysis,
        "explanation": explanation
    }
