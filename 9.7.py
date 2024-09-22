def is_prime(func):
    def wrapper(n1, n2, n3):
        total = func(n1, n2, n3)
        count = 0
        for i in range(1, total + 1):
            if total % i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return total
    return wrapper

@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3


result = sum_three(2, 3, 6)
print(result)
