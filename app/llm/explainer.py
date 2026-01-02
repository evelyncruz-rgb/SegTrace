from app.llm.client import call_llm

SYSTEM_PROMPT = """
You are a systems debugging assitant.
You explain runtime crashes using GDB output.
Do not speculate beyond the provided data.
"""

def explain_crash(analysis: dict, source_code: str | None = None):
    prompt = f""" 
Program crashed with the following details:

Signal:
{analysis.get("signal")}

Faulting function:
{analysis.get("function")}

Faulting line:
{analysis.get("line")}

Backtrace:
{analysis.get("backtrace")}

Explain:
1. Why the crash occurred at this point
2. What memory/state is invalid
3. What specific code change would fix it
"""
    if source_code:
        prompt += f"\nSource code:\n{source_code}"

    return call_llm(SYSTEM_PROMPT, prompt)
