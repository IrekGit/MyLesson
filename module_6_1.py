class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True


Wolf = Predator('Волк с Уолл-Стрит')
Dog = Mammal('Хатико')
C_7 = Flower('Цветик семицветик')
Orange = Fruit('Заводной апельсин')

print(Wolf.name, C_7.name)
print(Dog.name, Orange.name)

print(Wolf.alive)
print(Dog.fed)

Wolf.eat(C_7)
Dog.eat(Orange)

print(f"{Wolf.name} накормлен: {Wolf.fed}, жив: {Wolf.alive}")
print(f"{Dog.name} накормлен: {Dog.fed}, жив: {Dog.alive}")