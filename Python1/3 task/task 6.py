num = input("Введите последовательность целых чисел через пробел: ")
numlist = list(map(int, num.split()))

copy = len(numlist) != len(set(numlist))

print(copy)