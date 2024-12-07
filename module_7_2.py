def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Получаем текущую позицию байта
            start_position = file.tell()
            # Записываем строку в файл
            file.write(string + '\n')
            # Записываем в словарь номер строки и позицию в байтах
            strings_positions[(index + 1, start_position)] = string

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
