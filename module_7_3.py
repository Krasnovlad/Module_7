import os.path


class WordsFinder:
    file_names = []

    def __init__(self, *file_names):
        directory = 'text_files'
        file_names = [os.path.join(directory, file) for file in file_names]
        self.file_names = file_names

    def get_all_words(self) -> dict:
        files_dict = {}

        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                all_words = []

                for line in f:
                    words_list = line.split()

                    for word in words_list:
                        if word == '-':
                            continue

                        all_words.append(word.lower().translate(str.maketrans('', '', '!?;:=.,')))

                files_dict[os.path.basename(f.name)] = all_words
        return files_dict

    def find(self, word) -> dict:
        result = {}

        iterator_words = iter(self.get_all_words().items())
        key, value = next(iterator_words)
        result[key] = value.index(word.lower()) + 1
        return result

    def count(self, word) -> dict:
        result = {}

        iterator_words = iter(self.get_all_words().items())
        key, value = next(iterator_words)
        result[key] = value.count(word.lower())
        return result


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего