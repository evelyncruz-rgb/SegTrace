import subprocess

def run_gdb(binary_path: str) -> dict:
    result = subprocess.run(
        [
            "gdb",
            "-batch",
            "-ex", "run",
            "-ex", "bt",
            "--args", binary_path
        ],
        capture_output=True,
        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }