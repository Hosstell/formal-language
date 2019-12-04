from typing import List


class StateMachine:
    def __init__(self, graph: dict = {}, start_state: int = 0, end_states: List[int] = [0]):
        self.graph = graph
        self.start_state = start_state
        self.end_states = end_states
        self.state = None

    def add(self, new_state: int, new_actions: dict):
        if new_state in self.graph.keys():
            graph_state = self.graph[new_state]
            for new_action_key in new_actions.keys():
                graph_state[new_action_key] = new_actions[new_action_key]
        else:
            self.graph[new_state] = new_actions

    def delete_state(self, state):
        return self.graph.pop(state)

    def delete_connection(self, state, action):
        return self.graph[state].pop(action)

    def check(self, line):
        self.state = self.start_state

        for letter in line:
            self.state = self.graph[self.state][letter]

        return self.state in self.end_states


if __name__ == '__main__':
    graph = {
        0: {
            '0': 1,
        },
        1: {
            '1': 2
        },
        2: {
            '2': 1
        }
    }
    start_state = 0
    end_states = [1]

    sm = StateMachine(graph, start_state, end_states)

    print(sm.check('012'))
    print(sm.check('012121212'))
