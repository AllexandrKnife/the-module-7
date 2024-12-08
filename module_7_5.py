import os
import time

# Укажите путь к каталогу, который нужно обойти
directory = "."  # Текущая директория проекта

# Обход каталога с помощью os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формирование полного пути к файлу
        filepath = os.path.join(root, file)

        # Получение времени последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получение размера файла
        filesize = os.path.getsize(filepath)

        # Получение родительской директории файла
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, '
              f'Путь: {filepath}, '
              f'Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
