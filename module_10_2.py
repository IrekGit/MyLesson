import threading
import time

class Knight(threading.Thread):
    warrior = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.warrior:
            if self.warrior <= 0:
                break
            self.warrior -= self.power
            self.days += 1
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.warrior} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

# Создание объектов-рыцарей
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод завершения всех битв
print("Все битвы закончились!")