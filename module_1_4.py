my_string = input('Пожалуйста, введите какую-нибудь небольшую строку текста: ')
print("Количество символов в введенной Вами строке:", len(my_string))
print("Преобразуем строку в верхний регистр:", my_string.upper())
print("Преобразуем строку в нижний регистр:", my_string.lower())
print("Удалим пробелы:", my_string.replace(' ',''))
print("Первый символ строки:", my_string[0])
print("Последний символ строки:", my_string[-1])