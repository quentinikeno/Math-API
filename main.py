from typing import Union
from fastapi import FastAPI
from services import equations

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Math API.  Go to /docs for documentation."}

@app.get("/add")
def read_item(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).add()

@app.get("/sub")
def read_item(minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99, negative: bool = False):
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond, negative).sub()