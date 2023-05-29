# Tests for equations.py

import pytest
from services import equations
   
def test_add_default():
    """Test the add method with the default settings."""
    
    result = equations.Generator().add()
    
    assert "first" in result
    assert result["first"] >= 1
    assert result["first"] <= 99
    assert "second" in result
    assert result["second"] >= 1
    assert result["second"] <= 99
    assert result["operation"], "+"
    assert result["expression"], f'{result["first"]} + {result["second"]}'
    assert result["answer"], result["first"] + result["second"]
    
def test_add_custom():
    """Test the add method with the min and max set to 2 and 3 for the first and second numbers."""
    
    result = equations.Generator(2, 3, 2, 3).add()
    
    assert "first" in result
    assert result["first"] >= 2
    assert result["first"] <= 3
    assert "second" in result
    assert result["second"] >= 2
    assert result["second"] <= 3
    assert result["operation"], "+"
    assert result["expression"] == f'{result["first"]} + {result["second"]}'
    assert result["answer"] == result["first"] + result["second"]
    
def test_sub_default():
    """Test the sub method with the default settings."""
    
    result = equations.Generator().sub()

    assert "first" in result
    assert result["first"] >= 1
    assert result["first"] <= 99
    assert "second" in result
    assert result["second"] >= 1
    assert result["second"] <= 99
    assert result["operation"], "-"
    assert result["expression"] == f'{result["first"]} - {result["second"]}'
    assert result["answer"] == result["first"] - result["second"]
    
def test_sub_negative():
    """Test the sub method with negative numbers."""
    
    result = equations.Generator(1, 2, 3, 4, True).sub()

    assert "first" in result
    assert result["first"] >= 1
    assert result["first"] <= 2
    assert "second" in result
    assert result["second"] >= 3
    assert result["second"] <= 4
    assert result["operation"] == "-"
    assert result["expression"] == f'{result["first"]} - {result["second"]}'
    assert result["answer"] == result["first"] - result["second"]
    assert result["answer"] < 0
    
def test_sub_negative_not_allowed():
    """Test the sub method when negatives are not allowed.  If the difference is negative the first and second numbers will switch so that the answer is positive."""
    
    result = equations.Generator(1, 1, 2, 2, False).sub()

    assert result["first"] == 2
    assert result["second"] == 1
    assert result["operation"] == "-"
    assert result["expression"] == f'{result["first"]} - {result["second"]}'
    assert result["answer"] == result["first"] - result["second"]
    assert result["answer"] == 1
    
def test_mul_default():
    """Test the mul method with the default settings."""
    
    result = equations.Generator().mul()

    assert "first" in result
    assert result["first"] >= 1
    assert result["first"] <= 99
    assert "second" in result
    assert result["second"] >= 1
    assert result["second"] <= 99
    assert result["operation"] == "*"
    assert result["expression"] == f'{result["first"]} * {result["second"]}'
    assert result["answer"] == result["first"] * result["second"]
    
def test_mul_custom():
    """Test the mul method with the custom settings."""
    
    result = equations.Generator(4, 4, 5, 5).mul()

    assert "first" in result
    assert result["first"], 4
    assert "second" in result
    assert result["second"], 5
    assert result["operation"] == "*"
    assert result["expression"] == f'{result["first"]} * {result["second"]}'
    assert result["answer"], 20
    
def test_find_divisors_of_30():
    """Test the find_divisors on finding the divisors of 30."""
    divisors = equations.Generator(30, 30).find_divisors()
    expected_divisors = [1, 30, 2, 15, 3, 10, 5, 6]
    assert all(item in divisors for item in expected_divisors)
    assert all(item in expected_divisors for item in divisors)
    
def test_find_divisors_of_negative_30():
    """Test the find_divisors on finding the divisors of -30."""
    divisors = equations.Generator(-30, -30).find_divisors()
    expected_divisors = [1, 30, 2, 15, 3, 10, 5, 6, -1, -30, -2, -15, -3, -10, -5, -6]
    assert all(item in divisors for item in expected_divisors)
    assert all(item in expected_divisors for item in divisors)
    
def test_find_divisors_of_36():
    """Test the find_divisors on finding the divisors of 36."""
    divisors = equations.Generator(36, 36).find_divisors()
    expected_divisors = [1, 36, 2, 18, 3, 12, 4, 9, 6]
    assert all(item in divisors for item in expected_divisors)
    assert all(item in expected_divisors for item in divisors)
    
def test_find_divisors_of_negative_36():
    """Test the find_divisors on finding the divisors of 36."""
    divisors = equations.Generator(-36, -36).find_divisors()
    expected_divisors = [1, 36, 2, 18, 3, 12, 4, 9, 6, -1, -36, -2, -18, -3, -12, -4, -9, -6]
    assert all(item in divisors for item in expected_divisors)
    assert all(item in expected_divisors for item in divisors)
    
def test_divisors_of_0():
    """Test that find divisors will raise an exception when the first number is 0."""
    with pytest.raises(ValueError):
        equations.Generator(0, 0).find_divisors()
        
def test_div_default():
    """Test the div method with the default settings."""
    
    result = equations.Generator().div()

    assert "first" in result
    assert result["first"] >= 1
    assert result["first"] <= 99
    assert "second" in result
    assert result["second"] >= 1
    assert result["second"] <= 99
    assert result["operation"], "/"
    assert result["expression"] == f'{result["first"]} / {result["second"]}'
    assert result["answer"] == result["first"] / result["second"]
    
def test_div_custom():
    """Test the div method with the custom settings.  Check that a new divisor is found if the second number doesn't divide the first evenly."""
    
    result = equations.Generator(20, 20, 19, 19).div()

    assert "first" in result
    assert "second" in result
    assert result["second"] != 19
    assert result["first"] % result["second"] == 0
    assert result["answer"] == result["first"] / result["second"]
    assert type(result["answer"]) == int
    
def test_div_default():
    """Test the div method with 0 set the the second number.  The second number should be randomized so that we avoid division by 0."""
    
    result = equations.Generator(1, 99, 0, 0).div()

    assert "second" in result
    assert result["second"] >= 1
    assert result["second"] <= 99
    
def test_random():
    """Test the random method.  It should return either a addition, subtraction, multiplication, or division problem."""
    
    result = equations.Generator().random()
    
    assert result["operation"] in ["+", "-", "*", "/"]
