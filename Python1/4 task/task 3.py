def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

a, b = map(int, input("напишите два числа через пробел   ").split())
result = euclid(a, b)
print(result)