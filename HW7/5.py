import random
import math

class MathUtils:
    @staticmethod
    def factorial(n):
        return math.factorial(n)

    @classmethod
    def generate_random(cls, start, end):
        return random.randint(start, end)

print(MathUtils.factorial(5))
print(MathUtils.generate_random(1, 10))
