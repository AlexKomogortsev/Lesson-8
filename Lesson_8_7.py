# Task 7

class ComplexNumber:

    def __init__(self, num: float):
        self.num = num

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return ComplexNumber(self.num + other.num)

    def __mul__(self, other):
        return ComplexNumber(self.num * other.num)



number_1 = ComplexNumber(-2.2563)
number_2 = ComplexNumber(3.4875)
number_3 = ComplexNumber(-1.21111)
number_4 = number_1 + number_2 * number_3
number_5 = number_4 * number_1
print(number_5)