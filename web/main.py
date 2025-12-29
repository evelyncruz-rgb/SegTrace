from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import shutil
import uuid
from app.pipeline import run_pipeline

app = FastAPI()
templates = Jinja2Templates(directory="web/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_class=HTMLResponse)
def analyze_code(
    request: Request, 
    file: UploadFile = File(None),
    code: str = Form(None)
):
    # Generate a unique filename
    filename = f"sandbox/input_{uuid.uuid4().hex}.c"

    if file and file.filename:
        with open(filename, "wb") as f:
            shutil.copyfileobj(file.file, f)
    elif code and code.strip():
        with open(filename, "w") as f:
            f.write(code)
    else:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request, 
                "result": "No input provided"
            }
    )

    try:
        result = run_pipeline(filename)
    except Exception as e:
        result = f"INTERNAL ERROR:\n{e}"

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "result": result}
    )