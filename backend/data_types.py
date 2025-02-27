from pydantic import BaseModel


class CodeInput(BaseModel):
    language: str
    code: str
    stdinput: str


class CodeRequest(BaseModel):
    prompt: str
