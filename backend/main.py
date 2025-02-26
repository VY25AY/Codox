from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from run_code import run_code as code_runner
from automated_gen import generate_code as ai_code_generator


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

class CodeInput(BaseModel):
    language: str
    code: str


@app.post("/run-code/")
def run_code(code_input: CodeInput):
    result = code_runner(code=code_input.code, language=code_input.language)
    return {"message": "Code received successfully", "language": code_input.language, "code": code_input.code, "result": result}


class CodeRequest(BaseModel):
    prompt: str

@app.post("/generate-code/")
def generate_code(code_request: CodeRequest):
    result = ai_code_generator(prompt=code_request.prompt)
    return {"message": "Code generated successfully", "prompt": code_request.prompt, "result": result}
