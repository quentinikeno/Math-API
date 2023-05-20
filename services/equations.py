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
    def __init__(self, minFirst = defaultMin, maxFirst = defaultMax, minSecond = defaultMin, maxSecond = defaultMax, negative = False):
        self.first = randint(minFirst, maxFirst)
        self.second = randint(minSecond, maxSecond)
        self.negative = negative

    def add(self) -> Equation:
        """Returns a dictionary with the type of the class Equation for an addtion problem."""
        operation = "+"
        expression = f"{self.first} {operation} {self.second}"
        answer = self.first + self.second
        return {"first": self.first, "second": self.second, "operation": operation, "expression": expression, "answer": answer}
    
    def sub(self) -> Equation:
        """Returns a dictionary with the type of the class Equation for subtraction problem problem."""
        operation = "-"
        if(self.first - self.second < 0 and self.negative == False):
            # Switch the first and second number if the difference is negative and negatives aren't allowed
            self.first, self.second = self.second, self.first
        expression = f"{self.first} {operation} {self.second}"
        answer = self.first + self.second
        return {"first": self.first, "second": self.second, "operation": operation, "expression": expression, "answer": answer}