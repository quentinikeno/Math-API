# Tests for the routes in main.py

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
    """Test the root (/) route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to the Math API!  Go to /docs for documentation."}
    
def test_add_default():
    """Test the /add route with the default settings.  Nothing passed into the query string."""
    response = client.get("/add")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '+'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_add_one_plus_one():
    """Test the /add route specifying 1 and 1 for the first and second numbers."""
    response = client.get("/add?minFirst=1&maxFirst=1&minSecond=1&maxSecond=1")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '+'
    assert problem['expression'] == '1 + 1'
    assert problem['answer'] == 2
    
def test_add_min_and_max():
    """Test the /add route specifying 1 and 1 for the first and second numbers using the min and max parameters.  It should override the other parameters."""
    response = client.get("/add?min=1&max=1&minFirst=3&maxSecond=5")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '+'
    assert problem['expression'] == '1 + 1'
    assert problem['answer'] == 2
    
def test_add_max_less_than_min():
    """Test the /add route when the max < min. The min and max should swap so that max > min."""
    response = client.get("/add?min=1&max=0")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] <= 1
    assert problem['first'] >= 0
    assert problem['second'] <= 1
    assert problem['second'] >= 0
    
def test_sub_default():
    """Test the /sub route with the default settings.  Nothing passed into the query string."""
    response = client.get("/sub")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '-'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_sub_one_minus_one():
    """Test the /sub route specifying 1 and 1 for the first and second numbers."""
    response = client.get("/sub?minFirst=1&maxFirst=1&minSecond=1&maxSecond=1")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '-'
    assert problem['expression'] == '1 - 1'
    assert problem['answer'] == 0
    
def test_sub_one_minus_2():
    """Test the /sub route specifying 1 and 2 for the first and second numbers respectively.  Negatives have been set to True."""
    response = client.get("/sub?minFirst=1&maxFirst=1&minSecond=2&maxSecond=2&negative=True")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 2
    assert problem['operation'] == '-'
    assert problem['expression'] == '1 - 2'
    assert problem['answer'] == -1
    
def test_sub_min_and_max():
    """Test the /sub route specifying 1 and 1 for the first and second numbers using the min and max parameters.  It should override the other parameters."""
    response = client.get("/sub?min=1&max=1&minFirst=3&maxSecond=5")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '-'
    assert problem['expression'] == '1 - 1'
    assert problem['answer'] == 0
    
def test_sub_max_less_than_min():
    """Test the /sub route when the max < min. The min and max should swap so that max > min."""
    response = client.get("/sub?min=1&max=0")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] <= 1
    assert problem['first'] >= 0
    assert problem['second'] <= 1
    assert problem['second'] >= 0
    
def test_mul_default():
    """Test the /mul route with the default settings.  Nothing passed into the query string."""
    response = client.get("/mul")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '*'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_mul_two_times_two():
    """Test the /sub route specifying 2 and 2 for the first and second numbers."""
    response = client.get("/mul?minFirst=2&maxFirst=2&minSecond=2&maxSecond=2")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 2
    assert problem['second'] == 2
    assert problem['operation'] == '*'
    assert problem['expression'] == '2 * 2'
    assert problem['answer'] == 4
    
def test_mul_min_and_max():
    """Test the /mul route specifying 1 and 1 for the first and second numbers using the min and max parameters.  It should override the other parameters."""
    response = client.get("/mul?min=1&max=1&minFirst=3&maxSecond=5")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '*'
    assert problem['expression'] == '1 * 1'
    assert problem['answer'] == 1
    
def test_mul_max_less_than_min():
    """Test the /mul route when the max < min. The min and max should swap so that max > min."""
    response = client.get("/mul?min=1&max=0")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] <= 1
    assert problem['first'] >= 0
    assert problem['second'] <= 1
    assert problem['second'] >= 0
    
def test_div_default():
    """Test the /div route with the default settings.  Nothing passed into the query string."""
    response = client.get("/div")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '/'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_div_two_divided_by_two():
    """Test the /div route specifying 2 and 2 for the first and second numbers."""
    response = client.get("/div?minFirst=2&maxFirst=2&minSecond=2&maxSecond=2")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 2
    assert problem['second'] == 2
    assert problem['operation'] == '/'
    assert problem['expression'] == '2 / 2'
    assert problem['answer'] == 1
    
def test_div_division_by_zero():
    """Test the /div route specifying 0 for the divison number.  Since division by 0 is not allowed, the number should be regenerated."""
    response = client.get("/div?minFirst=2&maxFirst=2&minSecond=0&maxSecond=0")
    problem = response.json()
    assert response.status_code == 200
    assert problem['second'] != 0
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] == '/'
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_div_min_and_max():
    """Test the /div route specifying 1 and 1 for the first and second numbers using the min and max parameters.  It should override the other parameters."""
    response = client.get("/div?min=1&max=1&minFirst=3&maxSecond=5")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    assert problem['operation'] == '/'
    assert problem['expression'] == '1 / 1'
    assert problem['answer'] == 1
    
def test_div_max_less_than_min():
    """Test the /div route when the max < min. The min and max should swap so that max > min.  The second number might be generated using the find_divisors method so no need to check that."""
    response = client.get("/div?min=4&max=2")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] <= 4
    assert problem['first'] >= 2
    
def test_random_default():
    """Test the /random route with the default settings.  Nothing passed into the query string."""
    response = client.get("/random")
    problem = response.json()
    assert response.status_code == 200
    assert type(problem['first']) == int
    assert type(problem['second']) == int
    assert problem['operation'] in ['+', '-', '*', '/']
    assert type(problem['expression']) == str
    assert type(problem['answer']) == int
    
def test_random_min_and_max():
    """Test the /random route specifying 1 and 1 for the first and second numbers using the min and max parameters.  It should override the other parameters."""
    response = client.get("/random?min=1&max=1&minFirst=3&maxSecond=5")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] == 1
    assert problem['second'] == 1
    
def test_random_max_less_than_min():
    """Test the /random route when the max < min. The min and max should swap so that max > min.  The second number might be generated using the find_divisors method so no need to check that."""
    response = client.get("/random?min=4&max=2")
    problem = response.json()
    assert response.status_code == 200
    assert problem['first'] <= 4
    assert problem['first'] >= 2