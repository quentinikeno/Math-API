from random import randint

defaultMax = 99
defaultMin = 1

class Equations:
    def __init__(self, maxFirst = defaultMax, minFirst = defaultMin, maxSecond = defaultMax, minSecond = defaultMin, negative = False):
        self.first = randint(minFirst, maxFirst)
        self.second = randint(minSecond, maxSecond)
        self.negative = negative

    def add(self):
        operation = "+"
        expression = f"{self.first} {self.operation} {self.second}"
        answer = self.first + self.second
        return {self.first, self.second, operation, expression, answer}