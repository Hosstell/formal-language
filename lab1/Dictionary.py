from typing import List
from RussianAlphabet import RussianAlphabet
from Alphabet import Alphabet
import time


class Dictionary:
    def __init__(self, alphabet: Alphabet, words=[]):
        self.__alphabet = alphabet()
        self.__words = words

    @property
    def size(self) -> int:
        return len(self.__words)

    @property
    def word_list(self) -> List[str]:
        word_list = list(self.__words)
        return word_list

    def __str__(self):
        return str(self.__words)

    def add_word(self, word):
        self.check_word(word)
        if word not in self.__words:
            self.__words.append(word.upper())

    def delete_word(self, word):
        self.__words.remove(word.upper())

    def filter(self, filter_word):
        filtered_words = list(filter(lambda x: filter_word.upper() in x, self.__words))
        return Dictionary(alphabet=type(self.__alphabet), words=filtered_words)

    def sort(self, desc=False):
        self.__words.sort()
        if desc:
            self.__words = self.__words[::-1]

        return self

    def check_word(self, word):
        if not self.__alphabet.check_word(word):
            raise Exception('В слове "{}" есть буква, которой нет в алфавите словаря'.format(word))


if __name__ == '__main__':
    russian_dictionary = Dictionary(RussianAlphabet)

    print('До добавления слова в словарь')
    print('Словарь:', russian_dictionary)
    print()

    russian_dictionary.add_word('Яблоко')
    russian_dictionary.add_word('Груша')
    russian_dictionary.add_word('Вишня')
    russian_dictionary.add_word('Малина')
    russian_dictionary.add_word('Клубника')
    print('После добавления слов')
    print('Словарь:', russian_dictionary)
    print()

    russian_dictionary.delete_word('Клубника')
    print('После удаление слова "Клубника"')
    print('Словарь:', russian_dictionary)
    print()

    filtered_russian_dictionary = russian_dictionary.filter('ш')
    print('После фильтрации по букве "ш"')
    print('Словарь:', filtered_russian_dictionary)
    print()

    print('После сортировки словаря')
    print('Словарь до:', russian_dictionary)
    print('Словарь после:', russian_dictionary.sort())
    print('Словарь обратно:', russian_dictionary.sort(desc=True))
    print()

    print('Добавление английского слова "Cat"')
    time.sleep(0.5)
    russian_dictionary.add_word('Cat')
