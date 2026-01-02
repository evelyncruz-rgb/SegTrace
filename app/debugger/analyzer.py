def analyze(gdb_output: dict) -> dict:
    text = gdb_output["stdout"]

    if "SIGSEGV" in text:
        return {
            "type": "segmentation_fault",
            "likely_cause": "invalid memory access"
        }
    
    return {
        "type": "unknown",
        "likely_cause": "could not determine"
    }