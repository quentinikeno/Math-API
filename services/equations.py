from random import randint

defaultMax = 99
defaultMin = 1

class Equation:
    first: int
    second: int
    operation: str
    expression: str
    answer: int

class Equations:
    def __init__(self, maxFirst = defaultMax, minFirst = defaultMin, maxSecond = defaultMax, minSecond = defaultMin, negative = False):
        self.first = randint(minFirst, maxFirst)
        self.second = randint(minSecond, maxSecond)
        self.negative = negative

    def add(self) -> Equation:
        operation = "+"
        expression = f"{self.first} {operation} {self.second}"
        answer = self.first + self.second
        return {"first": self.first, "second": self.second, "operation": operation, "expression": expression, "answer": answer}