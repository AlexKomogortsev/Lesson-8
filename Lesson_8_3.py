# Task 3

class NoFloatException(Exception):
    def __init__(self, text):
        self.text = text


def get_float(a):
    try:
        a = float(a)
    except ValueError:
        raise NoFloatException('Пользователь, вводи только ЧИСЛА')
    return float(a)



l = []
enter = input('Введите первый элемент списка. В случае завершения процедуры, наберите "stop": ')
while enter.lower() != 'stop':
    try:
        get_float(enter)
    except Exception as err:
        print(err)
    else:
        l.append(get_float(enter))
    enter = input('Введите следующий элемент списка. В случае завершения процедуры, наберите "stop": ')
    continue
else:
    print(f'Список Ваших чисел равен: {l}')
