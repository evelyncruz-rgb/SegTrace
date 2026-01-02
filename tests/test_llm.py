from app.llm.client import call_llm

res = call_llm(
    "You are a helpful assistant.",
    "Explain why dereferencing a NULL pointer causes a crash."
)

print(res["text"])