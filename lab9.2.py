import string

input_str = input("Введіть рядок символів: ")

unique_chars = set(input_str)

letters_set = set()
digits_set = set()
punctuation_set = set()

for char in unique_chars:
    if char.isalpha():
        letters_set.add(char)
    elif char.isdigit():
        digits_set.add(char)
    elif char in string.punctuation:
        punctuation_set.add(char)

print("Унікальні символи:", "".join(unique_chars))
print("Літери:", letters_set)
print("Цифри:", digits_set)
print("Розділові знаки:", punctuation_set)
