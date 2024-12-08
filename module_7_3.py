import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read().lower()
                # Удаляем пунктуацию
                translator = str.maketrans('', '',
                                           string.punctuation.replace('-', ''))  # Убираем всю пунктуацию, кроме тире
                cleaned_text = text.translate(translator).replace(' - ', ' ')
                words = cleaned_text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Позиция (1-indexed)
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)  # Количество слов
        return result

# Пример работы с классом:
# Пример файла 'test_file.txt':
# "It's a text for the task НАЙТИ ВЕЗДЕ. Используйте его для самопроверки. Успехов в решении задачи. text text text."

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))      # 3 слово по счёту
# print(finder2.count('teXT'))     # 4 слова teXT в тексте всего
