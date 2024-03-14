number = input("Введите число в десятичном коде: ")

if int(number) > 0:
    decimalnumber = int(number)
#Двоичная
    binnum = bin(decimalnumber)
#Воьсиричная
    octnum = oct(decimalnumber)
#Шеснадцатеричная
    hexnum = hex(decimalnumber)

    print(f"Двоичное представление: {binnum}")
    print(f"Восьмеричное представление: {octnum}")
    print(f"Шестнадцатеричное представление: {hexnum}")
else:
    print("Неверный ввод")