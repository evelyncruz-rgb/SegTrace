from app.pipeline import run_pipeline

if __name__ == "__main__":
    result = run_pipeline("tests/valid.c")
    print(result)