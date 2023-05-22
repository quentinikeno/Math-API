from random import randint, choice

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
        divisors = [1]
        if self.first == 0:
            self.first = 1
        if self.first % self.second != 0:
            start = self.first if self.first < 0 else 1
            for i in range(start, int(self.first / 2) + 1):
                if self.first % i == 0:
                    divisors.append(i)
            lower_divisors = divisors
            for lower_divisor in lower_divisors:
                lower_divisors.append(self.first / lower_divisor)
            if self.first < 0:
                negative_divisors = divisors
                for negative_divisor in negative_divisors:
                    divisors.append(negative_divisor * -1)
            self.second = choice(divisors)
        operation = "/"
        expression = f"{self.first} {operation} {self.second}"
        answer = self.first * self.second
        return {"first": self.first, "second": self.second, "operation": operation, "expression": expression, "answer": answer}