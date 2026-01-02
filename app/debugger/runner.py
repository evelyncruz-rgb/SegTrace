import subprocess

def run(binary_path: str) -> dict:
    result = subprocess.run(
        [binary_path],
        capture_output=True,
        text=True
    )

    crashed = result.returncode < 0

    return {
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "crashed": crashed
    }
