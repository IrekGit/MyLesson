my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
i = 0
j = 0                           # счетчик положительных чисел
size_my_list = len(my_list)
while i < size_my_list and my_list[i] >= 0:
    if my_list[i] != 0:
        print(my_list[i])
        j = j + 1
    i = i + 1
    continue
print(f"Всего положительных чисел из списка (до первого отрицательного): {j}")
