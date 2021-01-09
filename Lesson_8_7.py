# Task 7

class ComplexNumber:

    def __init__(self, a1: float, a2, i):
        self.a1 = a1
        self.a2 = a2
        self.i = i

    def __str__(self):
        return f'{self.a1} + ({self.a2} * {self.i})'

    def __add__(self, other):
        self.a1 = self.a1 + other.a1
        self.a2 = self.a2 + other.a2
        return ComplexNumber(self.a1, self.a2, self.i)

    def __mul__(self, other):
        self.a1 = self.a1 * other.a1
        self.a2 = self.a2 * self.a2
        return ComplexNumber(self.a1, self.a2, self.i)



number_a = ComplexNumber(-2.2563, 3.456, 'i')
number_b = ComplexNumber(3.4875, - 2.142,  'i')
number_c = ComplexNumber(-1.21111, - 1.2567, 'i')
number_d = number_a + number_c
number_e = number_c * number_b
print(number_d)
print(number_e)