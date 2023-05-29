from typing import Union
from fastapi import FastAPI
from services import equations
from pydantic import BaseModel
from response_examples import add_responses, sub_responses, mul_responses, div_responses, random_responses

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
    return {"msg": "Welcome to the Math API!  Go to /docs for documentation."}

@app.get("/add", response_model = Equation, responses = add_responses)
def get_add(min: Union[int, None] = None, max: Union[int, None] = None, minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    """The addition route which responds with a random addition problem."""
    if type(min) == int:
       minFirst = min
       minSecond = min
    if type(max) == int:
       maxFirst = max
       maxSecond = max
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).add()

@app.get("/sub", response_model = Equation, responses = sub_responses)
def get_sub(min: Union[int, None] = None, max: Union[int, None] = None, minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99, negative: bool = False):
    """The subtraction route which responds with a random subtraction problem."""
    if type(min) == int:
       minFirst = min
       minSecond = min
    if type(max) == int:
       maxFirst = max
       maxSecond = max
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond, negative).sub()

@app.get("/mul", response_model = Equation, responses = mul_responses)
def get_mul(min: Union[int, None] = None, max: Union[int, None] = None, minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    """The multiplication route which responds with a random multiplication problem."""
    if type(min) == int:
       minFirst = min
       minSecond = min
    if type(max) == int:
       maxFirst = max
       maxSecond = max
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).mul()

@app.get("/div", response_model = Equation, responses = div_responses)
def get_div(min: Union[int, None] = None, max: Union[int, None] = None, minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99):
    """The division route which responds with a random division problem."""
    if type(min) == int:
       minFirst = min
       minSecond = min
    if type(max) == int:
       maxFirst = max
       maxSecond = max
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond).div()

@app.get("/random", response_model = Equation, responses = random_responses)
def get_random(min: Union[int, None] = None, max: Union[int, None] = None, minFirst: int = 1, maxFirst: int = 99, minSecond: int = 1, maxSecond: int = 99, negative: bool = False):
    """The random route which responds with an addtion, a subtraction, a multiplication, or a division problem."""
    if type(min) == int:
       minFirst = min
       minSecond = min
    if type(max) == int:
       maxFirst = max
       maxSecond = max
    return equations.Generator(minFirst, maxFirst, minSecond, maxSecond, negative).random()