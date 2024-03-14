num = input("Введите номер телефона: ")

numclean = ''.join(char for char in num if char.isdigit())

print(f"Очищенный номер телефона: {numclean}")