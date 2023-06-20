# Составить генератор (yield), который выводит из строки только цифры


def digits_only(string):
    for char in string:
        if char.isdigit():
            yield char


string = "abc123def456"
for digit in digits_only(string):
    print(digit, end="")