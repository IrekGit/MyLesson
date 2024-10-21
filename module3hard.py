def calculate_structure_sum(d_s):
    result_calculate = 0
    for i in d_s:
        if isinstance(i, int):      # целое число
            result_calculate = result_calculate + i
            continue
        if isinstance(i, str):      # строка
            result_calculate = result_calculate + len(i)
            continue
        if isinstance(i, list):     # [список]
            result_calculate = result_calculate + calculate_structure_sum(i)
            continue
        if isinstance(i, dict):     # {словарь из ключей: и значений}
            result_calculate = result_calculate + calculate_structure_sum(i.keys()) + calculate_structure_sum(i.values())
            continue
        if isinstance(i, tuple):    # (кортеж)
            result_calculate = result_calculate + calculate_structure_sum(i)
            continue
        if isinstance(i, set):      # {множество}
            result_calculate = result_calculate + calculate_structure_sum(i)
            continue
        else:
            return 0
    return result_calculate


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)