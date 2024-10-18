def send_email(message, recipient, sender='university.help@gmail.com'):
    check_email = [False, False]
    if '@' not in recipient and sender:         # если в адресе отсутствует спецсимвол @
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} с сообщением {message}')
    else:
        for i in [recipient, sender]:
            for j in ('.com', '.ru', '.net'):   # проверка на правильное окончание почтового адреса отправителя и адресата
                if i.find(j) != -1:
                    check_email.pop(False)
                    break
        if False in check_email:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} с сообщением {message}')
        else:
            # print(f'Адреса {sender} и {recipient} корректные')
            if sender == recipient:             # проверка на совпадение почтовых адресов отправителя и адресата
                print(f'Нельзя отправить письмо с сообщением {message} самому себе!')
            elif sender == 'university.help@gmail.com':     # проверка отправки со стандартного адреса по умолчанию
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient} с сообщением {message}')
            else:                               # проверка на нестандартный адрес отправителя
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient} с сообщением {message}')


send_email('"Привет Urban раз!"', 'urban@mail.ru')
send_email('"Привет Urban два!"', 'urban2mail.ru')
send_email('"Привет Urban три!"', 'urban@mail.su')
send_email('"Привет Urban четыре!"', 'university.help@gmail.com')
send_email('"Привет Urban пять!"', 'urban@mail.ru', 'help@gmail.com')
