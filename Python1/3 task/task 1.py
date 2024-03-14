a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

# Сортировка
sorted_numbers = sorted([a, b, c])

# Число по середине
middle_number = sorted_numbers[1]

print(f"Число, по середине: {middle_number}")