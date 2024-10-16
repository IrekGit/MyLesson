def count_calls():  # функция подсчета вызова функций
    global calls    # глобальная переменная, доступна во всех функциях
    calls += 1

def string_info(string):    # возвращает длину строки и саму строку в верх-м и нижн-м регистрах
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):    # ищем не только сроку в списке, но и подстроку в каждом элементе списка
    global search_result
    count_calls()
    list_to_search = list(map(str.lower, list_to_search))
    string = string.lower()
    for i in range(0, len(list_to_search)):
        if list_to_search[i].find(string) != -1:
            search_result = True
            break
        else:
            search_result = False
    return search_result


calls = 0
print(string_info('Так, проверочкА'))
print(is_contains('Хаб', ['Хабаровск', 'Хобот']))
print(is_contains('Хаб', ['ХАБАРОВСК', 'Кабак']))
print(is_contains('Хабаровск', ['Москва', 'Екатеринбург', 'Владивосток']))
print(calls)
