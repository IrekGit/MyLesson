# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    for j in range(0, i):
        if numbers[i] % numbers[j] == 0 and numbers[j] != 1: # проверка на нулевой остаток деления и делитель не единица
            not_primes.append(numbers[i])
            break
        else:
            if i - j == 1: # проверка, что дошли до последнего делителя, который дает остаток
                primes.append(numbers[i])
print(primes)
print(not_primes)