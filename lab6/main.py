class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, elem):
        self.children.append(elem)

    def print(self, level=0):
        print(' '*level, end='')
        print(self.value[0])

        for child in self.children:
            child.print(level+1)

        print(' ' * level, end='')
        print(self.value[1])


class StateMachineWithMemory:
    def __init__(self, graph, start_state, end_states):
        self.graph = graph
        self.start_state = start_state
        self.end_states = end_states
        self.state = None
        self.stack = []

    def check_line(self, line):
        self.state = self.start_state
        index = 0
        while index <= len(line):
            try:
                char = line[index]
            except IndexError:
                char = ''

            try:
                stack_state = self.stack[-1]
            except IndexError:
                stack_state = ''

            try:
                new_state, stack_action, next_to = self.graph[self.state][(char, stack_state)]
            except:
                try:
                    stack_state = '*'
                    new_state, stack_action, next_to = self.graph[self.state][(char, stack_state)]
                except:
                    return False

            self.state = new_state
            self.action_to_stack(stack_action)

            if next_to:
                index += 1

        return self.state in self.end_states

    def action_to_stack(self, action):
        if 'append' in action:
            method_name, input_data = action.split(' ')
            getattr(self.stack, method_name)(input_data)

        if 'pop' in action:
            getattr(self.stack, action)()

    def make_tree(self, line):
        ends = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        start = line[0]
        end = ends[start]

        main_node = Node(start + end)
        index = 1
        start_index = index
        while index < len(line) - 1:
            start = line[index]
            end = ends[start]
            while end != line[index]:
                index += 1

            main_node.add_child(self.make_tree(line[start_index:index + 1]))
            index += 1
            start_index = index

        return main_node


if __name__ == '__main__':
    graph = {
        0: {
            ('(', '*'): (0, 'append (', True),
            (')', '('): (0, 'pop', True),

            ('{', '*'): (0, 'append {', True),
            ('}', '{'): (0, 'pop', True),

            ('[', '*'): (0, 'append [', True),
            (']', '['): (0, 'pop', True),

            ('', ''): (1, '', True),
        },
        1: {

        }
    }
    start_state = 0
    end_states = [1]

    sm = StateMachineWithMemory(graph, start_state, end_states)

    print(sm.make_tree('([{()}{}])').print())

