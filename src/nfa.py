class NFA:
    def __init__(self):
        self.states = []
        self.start_state = None
        self.accept_state = None
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

    def set_accept_state(self, state):
        self.accept_state = state
        self.steps.append(f"Set accept state: {state}")

def regex_to_nfa(regex):
    nfa = NFA()
    state_stack = []
    operator_stack = []

    def process_operator():
        operator = operator_stack.pop()
        if operator == '*':
            prev_start, prev_end = state_stack.pop()
            start = nfa.add_state()
            end = nfa.add_state()
            nfa.add_transition(start, '', prev_start)
            nfa.add_transition(prev_end, '', prev_start)
            nfa.add_transition(prev_end, '', end)
            nfa.add_transition(start, '', end)
            state_stack.append((start, end))
        elif operator == '|':
            second_start, second_end = state_stack.pop()
            first_start, first_end = state_stack.pop()
            start = nfa.add_state()
            end = nfa.add_state()
            nfa.add_transition(start, '', first_start)
            nfa.add_transition(start, '', second_start)
            nfa.add_transition(first_end, '', end)
            nfa.add_transition(second_end, '', end)
            state_stack.append((start, end))
        elif operator == '.':
            second_start, second_end = state_stack.pop()
            first_start, first_end = state_stack.pop()
            nfa.add_transition(first_end, '', second_start)
            state_stack.append((first_start, second_end))

    for char in regex:
        if char.isalpha():
            start = nfa.add_state()
            end = nfa.add_state()
            nfa.add_transition(start, char, end)
            state_stack.append((start, end))
        elif char == '*':
            operator_stack.append(char)
            process_operator()
        elif char in {'|', '.'}:
            while operator_stack and operator_stack[-1] in {'|', '.'}:
                process_operator()
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                process_operator()
            operator_stack.pop()

    while operator_stack:
        process_operator()

    nfa.set_start_state(state_stack[0][0])
    nfa.set_accept_state(state_stack[0][1])
    return nfa
