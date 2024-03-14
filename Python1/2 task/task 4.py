def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    hex_chars = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal //= 16
    return hexadecimal

try:
    decimal = int(input("Введите натуральное число в десятичном формате: "))
    if decimal <= 0:
        print("Неверный ввод")
    else:
        binary = decimal_to_binary(decimal)
        octal = decimal_to_octal(decimal)
        hexadecimal = decimal_to_hexadecimal(decimal)
        print("Двоичное представление:", binary)
        print("Восьмеричное представление:", octal)
        print("Шестнадцатеричное представление:", hexadecimal)
except:
    print("Неверный ввод")


