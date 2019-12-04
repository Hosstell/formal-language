from typing import List


class StateMachine:
    def __init__(self, graph: dict = {}, start_state: int = 0, end_states: List[int] = [0]):
        self.graph = graph
        self.start_state = start_state
        self.end_states = end_states
        self.state = None

    def check_line(self, line):
        self.current_states = [self.start_state]

        for letter in line:
            self.current_states = self.get_next_states(letter, self.current_states)

        return any([elem in self.current_states for elem in self.end_states])

    def get_next_states(self, letter, states):
        new_states = []
        for state in states:
            if letter in self.graph[state].keys():
                new_states.extend(self.graph[state][letter])

        return list(set(new_states))


if __name__ == '__main__':
    # ab+[abc]c*[ab]
    graph = {
        0: {
            'a': [1]
        },
        1: {
            'b': [1, 2, 3, 4]
        },
        2: {
            'a': [5, 6, 7]
        },
        3: {
            'b': [5, 6, 7]
        },
        4: {
            'c': [5, 6, 7]
        },
        5: {
            'c': [5, 6, 7]
        },
        6: {
            'a': [8]
        },
        7: {
            'b': [8]
        },
        8: {

        }
    }
    start_state = 0
    end_states = [8]

    sm = StateMachine(graph, start_state, end_states)

    print(sm.check_line('abccccccccc'))