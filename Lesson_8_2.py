# Task 2

class ZeroException(Exception):
    def __init__(self, text):
        self.text = text

def zero_division(x, y):
    if y == 0:
        raise ZeroException('!!! Нет деления на Нуль !!!')
    return x / y

x = float(input('Введите Делимое: '))
y = float(input('Введите Делитель: '))

try:
    result = zero_division(x, y)
except Exception as err:
    print(err)
else:
    print(f'Результат равен: {result}')



