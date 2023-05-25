from random import randint, choice
from math import sqrt

defaultMax = 99
defaultMin = 1

class Equation:
    first: int
    second: int
    operation: str
    expression: str
    answer: int

class Generator:
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
        """Returns a dictionary with the type of the class Equation for a subtraction problem problem."""
        operation = "-"
        if(self.first - self.second < 0 and self.negative == False):
            # Switch the first and second number if the difference is negative and negatives aren't allowed
            self.first, self.second = self.second, self.first
        expression = f"{self.first} {operation} {self.second}"
        answer = self.first - self.second
        return {"first": self.first, "second": self.second, "operation": operation, "expression": expression, "answer": answer}
    
    def mul(self) -> Equation:
        """Returns a dictionary with the type of the class Equation for a multiplication problem problem."""
        operation = "*"
        expression = f"{self.first} {operation} {self.second}"
        answer = self.first * self.second
        return {"first": self.first, "second": self.second, "operation": operation, "expression": expression, "answer": answer}
    
    def div(self) -> Equation:
        """Returns a dictionary with the type of the class Equation for a division problem problem."""
        if self.first == 0:
            self.first = 1
        if self.first % self.second != 0:
            divisors = self.find_divisors()
            self.second = choice(divisors)
        operation = "/"
        expression = f"{self.first} {operation} {self.second}"
        answer = self.first * self.second
        return {"first": self.first, "second": self.second, "operation": operation, "expression": expression, "answer": answer}
    
    def find_divisors(self):
        """Method to help find all divisors of self.first.  Will return a list of all divisors."""
        if self.first == 0:
            raise ValueError("Cannot find divisors for 0.")
        divisors = []
        end = int(sqrt(abs(self.first))) + 1
        for i in range(1, end):
            if self.first % i == 0:
                divisors.append(i)
                divisors.append(abs(int(self.first / i)))
        if self.first < 0:
            positive_divisors = divisors.copy()
            for divisor in positive_divisors:
                divisors.append(-divisor)
        return divisors
        