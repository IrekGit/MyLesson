def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    str_number = str_number[1:]
    if len(str_number) != 0:
        return first * get_multiplied_digits(int(str_number))
    else:
        return first


input_number = int(input('Введите число, произведение цифр которого хотите получить: '))
multiplication_number = get_multiplied_digits(input_number)
print(f'Получите результат (нули в расчете не учитываются): {multiplication_number}')