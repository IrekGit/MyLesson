import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                self.lock.release()


    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)
            self.lock.release()


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
