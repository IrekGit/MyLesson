def check_House(check_object):
    if isinstance(check_object, House):
        return True
    else:
        print(f'Проверка выявила, что "{check_object}" не является объектом класса House')
        return False

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if check_House(other):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if check_House(other):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if check_House(other):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if check_House(other):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if check_House(other):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if check_House(other):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return (self)

    def __iadd__(self, value):
        self.number_of_floors += value
        return (self)

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return (self)


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Акация', 20)
h3 = ('Домик в деревне')

print(h1)
print(h2)
print(h1 == h2, "равно") # __eq__
print()

h2 = h2 + 10 # __add__
print(h1)
print(h2)
print(h1 == h2, "равно")
print()

h1 += 10 # __iadd__
print(h1)
print(h2)
print()

h2 = 10 + h2 # __radd__
print(h1)
print(h2)

print(h1 > h2, "больше") # __gt__
print(h1 >= h2, "больше или равно") # __ge__
print(h1 < h2, "меньше") # __lt__
print(h1 <= h2, "меньше или равно") # __le__
print(h1 != h2, "не равно") # __ne__
print()

print(h3)
print(h1 == h3)