# Math API

This is an API for generating random mathematical equations. I personally had been using the [xMathAPI](https://github.com/cheatsnake/xMath-api) until it became deprecated, so I decided to try and implement my own recreation.

## API Reference

Different routes will allow you to receive different types of math problems. You can choose from addition, subtraction, multiplication, division problems or a random choice of on of the four operations. The response will contain two numbers, the operation, the expression of the problem, and the answer.

#### Get an Addition Problem

```
  GET /add
```

#### Get a Subraction Problem

```
  GET /sub
```

#### Get an Multiplication Problem

```
  GET /mul
```

#### Get an Division Problem

```
  GET /div
```

#### Get an Random Problem

This route will return a single addition, subtraction, multiplication, or division problem.

```
  GET /random
```

### Parameters

Here are the parameters that can be provided in the query string. All parameters are optional.
Parameter | Type | Description
---|---|---
`min` | Integer | Sets the minimum value for the first and second numbers of the equation. This value will override the values of minFirst and minSecond if those are provided. If not provided the default value is 1.
`max` | Integer | Sets the maximum value for the first and second numbers of the equation. This value will override the values of maxFirst and maxSecond if those are provided. If not provided the default value is 99.
`minFirst` | Integer | Sets the minimum value for the first number of the equation. If not provided the default value is 1.
`maxFirst` | Integer | Sets the maximum value for the first number of the equation. If not provided the default value is 99.
`minSecond` | Integer | Sets the minimum value for the second number of the equation. If not provided the default value is 1.
`maxSecond` | Integer | Sets the maximum value for the second number of the equation. If not provided the default value is 99.
`negative` | Boolean | This parameter indicates whether negative answers are allowed for subtraction problems on the /sub and /random routes. "True" means that negatives are allowed, while "False" means they are not allowed. The default value is "False".

## Tech Stack

-   Python 3.8.10
-   [FastAPI](https://fastapi.tiangolo.com/)
-   Pytest

## Installation

First clone or download this repository.

Next in the directory where the project is located, create a virtual environment and install the requirements using PIP.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then start the server with uvicorn:

```
uvicorn main:app
```

## Running Tests

To run tests, first install requirements_dev.txt. This will install Pytest if you don't already have it.

```
pip install -r requirements_dev.txt
```

Then run Pytest.

```
pytest
```

## Authors

-   [Quentin Ikeno](https://github.com/quentinikeno)
