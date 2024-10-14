# Составьте алгоритм, используя циклы, чтобы в независимости от введённого
# числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа
import time
def check_input(n):
    if n > 2 and n < 21:
        return True
    else:
        return False


check_ = False
while check_ == False:
    n = int(input('Введите число в диапазоне от 3 до 20: '))
    if check_input(n):
        check_ = True
        print('Принято в работу, ожидайте результат!')
    else:
        print('Условие по диапазону не выполнено!')

password_ = []
for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0 and i < j:
            password_.append(i)
            password_.append(j)
result = int(''.join(map(str, password_)))
time.sleep(n/6)
print(f'Пароль для числа {n}: {result}')