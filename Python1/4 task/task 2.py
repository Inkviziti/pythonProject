def Step(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return Step(a * a, n // 2)
    else:
        return (a * Step(a, n - 1))

a, n = map(int, input("Введите два числа через пробел   ").split())
result = Step(a, n)
print(result)