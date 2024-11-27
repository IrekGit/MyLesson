def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        iter(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

    try:
        total_sum, incorrect_data = personal_sum(numbers)
        correct_count = len(numbers) - incorrect_data
        return total_sum / correct_count if correct_count > 0 else 0
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но символы - строки
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Только числа 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё корректно
