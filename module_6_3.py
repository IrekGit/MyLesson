import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    speed = 1

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] += dz * self.speed

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("No sound defined")


class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz * self.speed / 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
print(db.get_cords())

db.dive_in(6)
print(db.get_cords())

db.lay_eggs()