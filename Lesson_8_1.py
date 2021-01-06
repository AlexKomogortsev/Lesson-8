# Task 1

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

class Data:


    def __init__(self, data: str):
        self.data = data

    def make_int(self):
        l = self.data.split('-')
        for i in range(len(l)):
            l[i] = int(l[i])
        return l

    @staticmethod
    def validation(l):
        if l[0] in range(months.get(l[1]) + 1):
            l[0] = 'Correct day'
        else:
            l[0] = 'Incorrect day'
        if l[1] in range(1, 12 + 1):
            l[1] = 'Correct month'
        else:
            l[1] = 'Incorrect month'
        if l[2] in range(1900, 2015 + 1):
            l[2] = 'Correct year'
        else:
            l[2] = 'Incorrect year'
        return l



data_1 = Data(input('Введите дату в виде строки формата "день-месяц-год": '))
print(type(data_1.make_int()[0]))
print(Data.validation(data_1.make_int()))

