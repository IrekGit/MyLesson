first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    i = 3
elif first == second or second == third or first == third:
    i = 2
else:
    i = 0
print(f'Количество совпавших чисел: {i}')