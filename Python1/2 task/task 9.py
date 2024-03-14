def clean_phone_number(phone_number):
    valid_chars = "+0123456789"
    clean_number = ""
    for char in phone_number:
        if char in valid_chars:
            clean_number += char
    return clean_number

user_input = input("Введите номер телефона: ")
cleaned_number = clean_phone_number(user_input)
print(cleaned_number)