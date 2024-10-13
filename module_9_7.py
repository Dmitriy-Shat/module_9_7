def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        if number < 2:
            return f'{number} - не простое и не составное'
        for j in range(2, number + 1):
            if number % j == 0 and number != j:
               return f'{number} - не простое'
            elif number % j == 0 and number == j:
                return f'{number} - простое'
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result

result = sum_three(2, 5, 10)
print(result)