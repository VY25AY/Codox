from fastapi import FastAPI, HTTPException
from automated_gen import generate_code as ai_code_generator
from execute_code import execute_code as code_runner
from data_types import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,

    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}


@app.post("/run-code/")
def run_code(code_input: CodeInput):
    result = code_runner(
        code=code_input.code, language=code_input.language, stdinput=code_input.stdinput)
    return {"message": "Code received successfully", "language": code_input.language, "code": code_input.code, "result": result}


@app.post("/generate-code/")
def generate_code(code_request: CodeRequest):
    result = ai_code_generator(prompt=code_request.prompt)
    return {"message": "Code generated successfully", "prompt": code_request.prompt, "result": result}
