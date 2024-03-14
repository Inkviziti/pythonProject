def last_letters(words):
    result = ""
    for word in words:
        if len(word) > 0:
            result += word[-1]
    return result

word_list = []
n = int(input("Введите количество слов: "))
for _ in range(n):
    word = input("Введите слово: ")
    word_list.append(word)

output = last_letters(word_list)
print(output)