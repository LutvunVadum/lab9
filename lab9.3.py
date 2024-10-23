plants_dict = {
    'Сосна': 'Євразія',
    'Бамбук': 'Азія',
    'Евкаліпт': 'Австралія',
    'Кактус': 'Америка',
    'Оливкове дерево': 'Африка',
    'Тополя': 'Європа',
    'Дуб': 'Європа',
    'Баобаб': 'Африка',
    'Манго': 'Африка',
    'Липа': 'Європа',
    'Клен': 'Північна Америка',
    'Пальма': 'Азія'
}

english_plants_dict = {}

for plant in plants_dict:
    english_name = input(f"Введіть англійську назву для рослини '{plant}': ")
    english_plants_dict[plant] = english_name

print("\nСловник рослин і континентів:")
for plant, continent in plants_dict.items():
    print(f"{plant}: {continent}")

print("\nСловник рослин англійською мовою:")
for plant, english_name in english_plants_dict.items():
    print(f"{plant}: {english_name}")