from typing import Union
from fastapi import FastAPI
from services import equations
from pydantic import BaseModel

app = FastAPI()

class Equation(BaseModel):
    first: int
    second: int
    operation: str
    expression: str
    answer: int

# === Routes ===

@app.get("/")
def get_root():
    return {"msg": "Welcome to the Math API.  Go to /docs for documentation."}

@app.get("/add", response_model=Equation)
def get_add(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).add()

@app.get("/sub", response_model=Equation)
def get_sub(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99, negative: bool = False):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond, negative).sub()

@app.get("/mul", response_model=Equation)
def get_mul(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).mul()

@app.get("/div", response_model=Equation)
def get_div(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).div()

@app.get("/random", response_model=Equation)
def get_random(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99, negative: bool = False):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond, negative).random()