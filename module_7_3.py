class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for punct in punctuation_to_remove:
                    content = content.replace(punct, '')
                words = content.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)
            else:
                result[name] = -1

        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            result[name] = words.count(word)

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))