import subprocess
from pathlib import Path

def compile_c(source_path: str, output_path: str) -> dict:
    """
    Compile a C source file using gcc.

    Returns:
        {
            "success" : bool,
            "stdout" : str,
            "stderr" : str
        }
    """
    source = Path(source_path)
    output = Path(output_path)

    if not source.exists():
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Source file {source} does not exist"
        }

    result = subprocess.run(
        ["gcc", str(source), "-g", "-o", str(output)],
        capture_output=True,
        text=True
    )

    return {
        "success": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr
    }