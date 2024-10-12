immutable_var = (1, 2, 'number', True, [3, 4])
print(immutable_var)
# immutable_var[0] = 2 # Здесь ошибка - элемент Кортежа невозможно модифицировать!
mutable_list = [10, 20, 30, 'abc', False]
print(mutable_list)
mutable_list[0] = mutable_list[2] + 5
mutable_list[3] = list(mutable_list[3])
mutable_list[4] = True
mutable_list.remove(20)
print(mutable_list)