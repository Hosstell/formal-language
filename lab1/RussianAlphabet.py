from Alphabet import Alphabet


class RussianAlphabet(Alphabet):
    def __init__(self):
        letters = [
            'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
            'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
            'Э', 'Ю', 'Я'
        ]
        super().__init__(letters)


if __name__ == '__main__':
    russian_alphabet = RussianAlphabet()
    print(russian_alphabet)
