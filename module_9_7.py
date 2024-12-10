from sympy import isprime
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isprime(result):
            print("Простое")
        else:
            print("Составное")

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример:
result = sum_three(2, 3, 6)
print(result)