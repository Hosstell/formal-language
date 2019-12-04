from typing import List, Union
import time


class Alphabet:
    def __init__(self, letter_list=[]):
        self.__letters = set()
        self.add_letters(letter_list)

    @property
    def size(self) -> int:
        return len(self.__letters)

    @property
    def letter_list(self) -> List[str]:
        letter_list = list(self.__letters)
        letter_list.sort()
        return letter_list

    def __str__(self):
        letter_list = list(self.__letters)
        letter_list.sort()
        return ' '.join(letter_list)

    def add_letters(self, letters: List[str]) -> None:
        for letter in letters:
            self.add_letter(letter)

    def add_letter(self, letter: str) -> None:
        self.__check_letter(letter)
        self.__letters.add(letter.upper())

    def remove_letter(self, letter: str) -> None:
        letter = letter.upper()
        self.__letters.discard(letter)

    def __check_letter(self, letter: str) -> None:
        if not letter.isalpha():
            raise Exception("Символ '{}' не является буквой".format(letter))

    def has(self, letter: str) -> bool:
        return letter.upper() in self.__letters

    def check_word(self, word: str):
        for letter in word:
            if not self.has(letter):
                return False
        return True


if __name__ == '__main__':
    alphabet = Alphabet()
    print('Перед добавление буквы b')
    print('Алфавит:', alphabet.letter_list)
    print()

    alphabet.add_letter('b')
    print('После добавление буквы b')
    print('Алфавит:', alphabet.letter_list)
    print()

    alphabet.add_letters(['a', 'b', 'c', 'j', 'o', 'z', 'x', 't'])
    print('После добавление набора букв a,b,c,j,o,z,x,t')
    print('Алфавит:', alphabet.letter_list)
    print()

    alphabet.remove_letter('j')
    print('После удаления буквы j')
    print('Алфавит:', alphabet.letter_list)
    print()

    print('Алфавит:', alphabet.letter_list)
    print('Имеет ли алфавит букву "B"?', alphabet.has('b'))
    print('Имеет ли алфавит букву "Y"?', alphabet.has('Y'))
    print()

    print('Алфавит:', alphabet.letter_list)
    print('Можно ли написать слова "Cat"?', alphabet.check_word('Cat'))
    print('Можно ли написать слова "Mother"?', alphabet.check_word('Mother'))
    print()


    print('Попытка добавить в алфавит символ "$"')
    time.sleep(0.5)
    alphabet.add_letter('$')
