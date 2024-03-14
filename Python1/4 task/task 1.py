def check_num(num):
    uniq_num = set(num)
    if len(uniq_num) == 1:
        return "Все числа равны"
    elif len(uniq_num) == len(num):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

num = list(map(int, input("Введите числа через пробел    ").split()))
result = check_num(num)
print(result)