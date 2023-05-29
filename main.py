from typing import Union
from fastapi import FastAPI
from services import equations

app = FastAPI()

@app.get("/")
def get_root():
    return {"msg": "Welcome to the Math API.  Go to /docs for documentation."}

@app.get("/add")
def get_add(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).add()

@app.get("/sub")
def get_sub(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99, negative: bool = False):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond, negative).sub()

@app.get("/mul")
def get_mul(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).mul()

@app.get("/div")
def get_div(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).div()