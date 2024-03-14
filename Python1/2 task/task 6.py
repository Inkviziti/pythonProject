def check_zeros_and_ones(s):
    zeros = s.count('0')
    ones = s.count('1')
    if zeros == ones:
        return "yes"
    else:
        return "no"

input_string = input("Введите строку из 0 и 1: ")
result = check_zeros_and_ones(input_string)
print(result)