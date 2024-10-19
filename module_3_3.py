def print_params(a = 1, b = 'строка', c = True):
    print(b, a, c)


# 1.Функция с параметрами по умолчанию:
print_params(2, "столбец", c = False)
print_params()
print_params(b = 25)
print_params(c = 'Истина', a = False, b = 33)
print_params(c = [1,2,3])

# 2.Распаковка параметров:
values_list = [7, 'Seven', True]
values_dict = {'a': 9, 'b': 'Urban', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [8, 'список']
print_params(*values_list_2, 42)