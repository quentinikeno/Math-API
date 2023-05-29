from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

class Equation:
    first: int
    second: int
    operation: str
    expression: str
    answer: int

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to the Math API.  Go to /docs for documentation."}
    
def test_add_default():
    response = client.get("/add")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '+'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_add_one_plus_one():
    response = client.get("/add?minFirst=1&maxFirst=1&minSecond=1&maxSecond=1")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '+'
    assert problem['expression'] == '1 + 1'
    assert problem['answer'] == 2
    
def test_sub_default():
    response = client.get("/sub")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '-'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_sub_one_minus_one():
    response = client.get("/sub?minFirst=1&maxFirst=1&minSecond=1&maxSecond=1")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '-'
    assert problem['expression'] == '1 - 1'
    assert problem['answer'] == 0
    
def test_sub_one_minus_2():
    response = client.get("/sub?minFirst=1&maxFirst=1&minSecond=2&maxSecond=2&negative=True")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 2
    assert problem['operation'] == '-'
    assert problem['expression'] == '1 - 2'
    assert problem['answer'] == -1
    
def test_mul_default():
    response = client.get("/mul")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '*'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_mul_two_times_two():
    response = client.get("/mul?minFirst=2&maxFirst=2&minSecond=2&maxSecond=2")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 2
    assert problem['second'] == 2
    assert problem['operation'] == '*'
    assert problem['expression'] == '2 * 2'
    assert problem['answer'] == 4
    
def test_div_default():
    response = client.get("/div")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '/'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_div_two_divided_by_two():
    response = client.get("/div?minFirst=2&maxFirst=2&minSecond=2&maxSecond=2")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 2
    assert problem['second'] == 2
    assert problem['operation'] == '/'
    assert problem['expression'] == '2 / 2'
    assert problem['answer'] == 1
    
def test_div_division_by_zero():
    response = client.get("/div?minFirst=0&maxFirst=0&minSecond=2&maxSecond=2")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] != 0
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '/'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int