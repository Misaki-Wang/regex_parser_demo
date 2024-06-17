import graphviz

class DFA:
    def __init__(self):
        self.states = []
        self.start_state = None
        self.accept_states = []
        self.transitions = {}
        self.steps = []  # 记录每一步的状态

    def add_state(self):
        state = len(self.states)
        self.states.append(state)
        self.transitions[state] = {}
        self.steps.append(f"Add state: {state}")
        return state

    def add_transition(self, from_state, input_char, to_state):
        if input_char not in self.transitions[from_state]:
            self.transitions[from_state][input_char] = []
        self.transitions[from_state][input_char].append(to_state)
        self.steps.append(f"Add transition: {from_state} --{input_char}--> {to_state}")

    def set_start_state(self, state):
        self.start_state = state
        self.steps.append(f"Set start state: {state}")

    def add_accept_state(self, state):
        self.accept_states.append(state)
        self.steps.append(f"Add accept state: {state}")

    def to_graphviz(self, filename="dfa"):
        dot = graphviz.Digraph(format='png')
        for state in self.states:
            if state == self.start_state:
                dot.node(str(state), shape='doublecircle', color='green')
            elif state in self.accept_states:
                dot.node(str(state), shape='doublecircle', color='red')
            else:
                dot.node(str(state), shape='circle')
        
        for from_state, transitions in self.transitions.items():
            for input_char, to_states in transitions.items():
                for to_state in to_states:
                    dot.edge(str(from_state), str(to_state), label=input_char)
        
        dot.render(filename)

def nfa_to_dfa(nfa):
    dfa = DFA()
    initial_state = frozenset([nfa.start_state])
    state_map = {initial_state: dfa.add_state()}
    unmarked_states = [initial_state]

    while unmarked_states:
        current = unmarked_states.pop()
        current_dfa_state = state_map[current]
        for input_char in set(char for state in current for char in nfa.transitions[state]):
            next_states = frozenset(
                next_state
                for state in current
                for next_state in nfa.transitions[state].get(input_char, [])
            )
            if not next_states:
                continue
            if next_states not in state_map:
                state_map[next_states] = dfa.add_state()
                unmarked_states.append(next_states)
            dfa.add_transition(current_dfa_state, input_char, state_map[next_states])
        if any(state == nfa.accept_state for state in current):
            dfa.add_accept_state(current_dfa_state)
    dfa.set_start_state(state_map[initial_state])
    return dfa