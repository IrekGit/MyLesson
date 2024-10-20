def single_root_words(root_word, *other_words):
    same_words = []
    list_other_words = list(map(str.lower, other_words))    # переводим кортеж в список, список - в нижний регистр
    root_word_lower = root_word.lower()                     # ключевое слово - в нижний регистр

    for i in range(len(other_words)):
         if root_word_lower in list_other_words[i]:         # ищем в списке слова, содержащие ключевое
            same_words.append(other_words[i])               # добавляем найденные слова в новый список
         elif list_other_words[i] in root_word_lower:       # также ищем в списке слова, входящие в состав ключевого
            same_words.append(other_words[i])               # также добавляем найденные слова в новый список
    return same_words


print(single_root_words('Прим', 'Пример', 'ПРИМОРЬЕ', 'ПРЕМЬЕРА', 'при', 'Премия', 'оПримус', 'Вот это Прима!'))
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)