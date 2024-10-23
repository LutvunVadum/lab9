data = ('Hello', 3.5, 4.8, 12, 7.2, 'Python', 5)

float_numbers = [x for x in data if isinstance(x, float)]

if float_numbers:
    average = sum(float_numbers) / len(float_numbers)
    print(f"Середнє арифметичне дійсних чисел: {average}")
else:
    print("У кортежі немає дійсних чисел.")
