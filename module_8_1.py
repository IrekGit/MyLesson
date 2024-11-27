def add_everything_up(a, b):
    try:
        return a + b

    except TypeError:
        print(f'"{a}" невозможно сложить с "{b}", но если надо - сложим!\nПрограммистам все можно!;)')
        return f'Вот результат: "{a}{b}"'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up([1, 2], [3, 4]))
print(add_everything_up('груша', [3, 4]))
print(add_everything_up('груша', 'персик'))