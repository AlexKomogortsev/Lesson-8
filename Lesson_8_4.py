# Task 4, 5, 6

from abc import ABC


class OfficeTech(ABC):

    def __init__(self, length: float, width: float, height: float, consumption: int):
        self.length = length
        self.width = width
        self.height = height
        self.consumption = consumption
        self.square = self.length * self.width
        self.volume = self.length * self.width * self.height
        self.value = 'new'


class Printer(OfficeTech):

    def __init__(self, length: float, width: float, height: float, consumption: int, paper: bool, dye: bool):
        super().__init__(length, width, height, consumption)
        self.paper = paper
        self.dye = dye

    @property
    def ready(self):
        if self.paper == True and self.dye == True:
            return True


class PC(OfficeTech):

    def __init__(self, length: float, width: float, height: float, consumption: int, memory: int, OS: str):
        super().__init__(length, width, height, consumption)
        self.memory = memory
        self.OS = OS

    @property
    def ready(self):
        if self.memory >= 2 and self.OS.lower() == 'windows':
            return True


class Projecter(OfficeTech):

    def __init__(self, length: float, width: float, height: float, consumption: int, canvas_height: int):
        super().__init__(length, width, height, consumption)
        self.canvas_height = canvas_height


class Room(ABC):
    tech_list = {}

    def __init__(self, length: float, width: float, height: float, max_consumption: int):
        self.length = length
        self.width = width
        self.height = height
        self.max_consumption = max_consumption
        self.square = self.length * self.width
        self.volume = self.length * self.width * self.height

    def __str__(self):
        return f'Имеется свободная площадь {self.square} м2 и свободный объем {self.volume} м3.\n' \
               f'Список техники, находящейся в помещении: {self.tech_list}'


class Store(Room):

    def __init__(self, length: float, width: float, height: float, max_consumption: int):
        super().__init__(length, width, height, max_consumption)
        self.tech_list = {
            'Printers': 0,
            'PCs': 0,
            'Projecters': 0
        }

    def add_tech_list(self, orgtech):
        if orgtech.__class__ == Printer:
            self.tech_list['Printers'] += 1
        elif orgtech.__class__ == PC:
            self.tech_list['PCs'] += 1
        elif orgtech.__class__ == Projecter:
            self.tech_list['Projecters'] += 1
        return self.tech_list

    def receive_tech(self, other):
        if self.square >= other.square and self.volume >= other.volume and self.height >= other.volume\
                and self.width >= other.width and self.length >= other.length:
            self.square -= other.square
            self.volume -= other.volume
            self.add_tech_list(other)
            other.value = 'store'
            return self.square, self.volume, self.tech_list
        else:
            print(f'Дорогой, на СКЛАДЕ места больше нет! Список того, что уже есть: {self.tech_list}')

    def reduce_tech_list(self, orgtech):
        if orgtech.__class__ == Printer and self.tech_list['Printers'] > 0:
            self.tech_list['Printers'] -= 1
        elif orgtech.__class__ == PC and self.tech_list['PCs'] > 0:
            self.tech_list['PCs'] -= 1
        elif orgtech.__class__ == Projecter and self.tech_list['Projecters'] > 0:
            self.tech_list['Projecters'] -= 1
        else:
            f'В помещении нет такой техники.'
        return self.tech_list


class OfficeRoom(Room):

    def __init__(self, length: float, width: float, height: float, max_consumption: int):
        super().__init__(length, width, height, max_consumption)
        self.tech_list = {
            'Printers': 0,
            'PCs': 0,
            'Projecters': 0
        }

    def add_tech_list(self, orgtech):
        if orgtech.__class__ == Printer:
            self.tech_list['Printers'] += 1
        elif orgtech.__class__ == PC:
            self.tech_list['PCs'] += 1
        elif orgtech.__class__ == Projecter:
            self.tech_list['Projecters'] += 1
        return self.tech_list

    def reduce_tech_list(self, orgtech):
        if orgtech.__class__ == Printer and self.tech_list['Printers'] > 0:
            self.tech_list['Printers'] -= 1
        elif orgtech.__class__ == PC and self.tech_list['PCs'] > 0:
            self.tech_list['PCs'] -= 1
        elif orgtech.__class__ == Projecter and self.tech_list['Projecters'] > 0:
            self.tech_list['Projecters'] -= 1
        elif self.tech_list['Printers'] == 0 or self.tech_list['PCs'] == 0 or self.tech_list['Projecters'] == 0:
            f'В помещении нет такой техники.'
        return self.tech_list

    def receive_tech(self, other, orgtech):
        if self.square >= orgtech.square and self.volume >= orgtech.volume and self.height >= orgtech.height \
                and self.width >= orgtech.width and self.length >= orgtech.length and orgtech.value == 'store':
            self.square -= orgtech.square
            self.volume -= orgtech.volume
            self.add_tech_list(orgtech)
            other.square += orgtech.square
            other.square += orgtech.volume
            other.reduce_tech_list(orgtech)
            orgtech.value = 'room'
            return self.square, self, self.tech_list
        else:
            print(f'Дорогой, либо на СКЛАДЕ нет техники, либо нет места в КОМНАТЕ!\n'
                  f'Список того, что тут уже вместилось: {self.tech_list}')


printer_1 = Printer(0.4, 0.4, 0.2, 10, True, True)
store_main = Store(5, 2, 3, 50)
store_main.receive_tech(printer_1)
printer_2 = Printer(0.3, 0.25, 0.22, 20, True, False)
store_main.receive_tech(printer_2)
projector_1 = Projecter(0.2, 0.25, 0.15, 30, 2)
store_main.receive_tech(projector_1)
sales_room = OfficeRoom(7, 6, 2.5, 100)
sales_room.receive_tech(store_main, projector_1)
PC_1 = PC(3, 1, 1, 10, 2, 'Windows')
PC_2 = PC(0.5, 1, 1, 10, 2, 'Windows')
PC_3 = PC(5, 1, 1, 10, 2, 'Windows')
Apple = PC(0.5, 0.5, 0.3, 10, 8, 'MacOS')
PC_5 = PC(0.5, 0.5,0.3, 10, 4, "Linux")
store_main.receive_tech(PC_1)
store_main.receive_tech(PC_2)
store_main.receive_tech(PC_3)
store_main.receive_tech(PC_5)
store_main.receive_tech(Apple)
print(store_main)
print(sales_room)
sales_room.receive_tech(store_main, PC_3)


