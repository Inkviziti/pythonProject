a, b, c = int(input("Введите 1 число   ")), int(input("Введите 2 число   ")), int(input("Введите 3 число   "))
if a > b and a < c :
    print(a)
elif a > c and a < b :
    print(a)
elif b > a and b < c :
    print(b)
elif b > c and b < a:
    print(b)
elif c > a and c < b:
    print(c)
elif c > b and c < a:
    print(c)
else:
    print(a, c, b)
    print("Есть одинаковвые цифры")