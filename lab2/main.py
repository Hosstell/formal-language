from lab1.Alphabet import Alphabet


class GramaticRule:
    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right

    def __str__(self):
        return '{} -> {}'.format(self.left, self.right)

    def execute(self, input_str: str, index=None):
        if index != None:
            new_str = input_str.replace(self.left, '', index)
            new_str = new_str.replace(' ', self.left, index-1)
            new_str = new_str.replace('__', self.right)
        else:
            new_str = input_str.replace(self.left, self.right)
        return new_str

    def type_1(self):
        return self.left <= self.right

    def type_2(self):
        return


class Gramatic:
    def __init__(self, terminal_list, not_terminal_list):
        self.__rules = []
        self.terminal = Alphabet(terminal_list)
        self.not_terminal = Alphabet(not_terminal_list)

    def add_rule(self, rule: GramaticRule):
        self.__check_adding(rule.left + rule.right)
        self.__rules.append(rule)

    def __check_adding(self, adding):
        for letter in adding:
            if not (self.terminal.has(letter) or self.not_terminal.has(letter)):
                raise Exception('Символ {} не определен в граматике'.format(letter))

    def delete_rule(self, left, right):
        deleting_rule = str(GramaticRule(left, right))
        self.__rules = list(filter(lambda x: str(deleting_rule) != str(x), self.__rules))

    def __str__(self):
        return '\n'.join(map(str, self.__rules))

    @property
    def type_number(self):
        results = [
            self.type_rule_1(),
            self.type_rule_2(),
            self.type_rule_3(),
            False
        ]
        return results.index(False)

    def type_rule_1(self):
        for rule in self.__rules:
            if len(rule.left) > len(rule.right):
                return False
        return True

    def type_rule_2(self):
        for rule in self.__rules:
            if not self.terminal.has(rule.left) or not len(rule.left) == 1:
                return False
        return True

    def type_rule_3(self):
        return any([
            self.check_left_side_grammatik(),
            self.check_right_side_grammatik()
        ])

    def check_left_side_grammatik(self):
        for rule in self.__rules:
            if len(rule.right) == 2:
                if not(self.terminal.has(rule.right[0]) and self.not_terminal.has(rule.right[1])):
                    return False
            if len(rule.right) == 1:
                if not self.not_terminal.has(rule.right[0]):
                    return False

            if len(rule.right) > 2:
                return False

        return True

    def check_right_side_grammatik(self):
        for rule in self.__rules:
            if len(rule.right) == 2:
                if not (self.not_terminal.has(rule.right[0]) and self.terminal.has(rule.right[1])):
                    return False
            if len(rule.right) == 1:
                if not self.not_terminal.has(rule.right[0]):
                    return False

            if len(rule.right) > 2:
                return False

        return True

    @property
    def type(self):
        return [
            'Граматика типа 0',
            'Контекстно-зависимая грамматика',
            'Контекстно-свободная грамматика',
            'Регулярная грамматика'
        ][self.type_number]

if __name__ == '__main__':
    a = GramaticRule('S', 'Ta')
    b = GramaticRule('T', 'Ta')

    g = Gramatic('ST', 'a')
    g.add_rule(a)
    g.add_rule(b)

    print(g.type_number, '-', g.type)