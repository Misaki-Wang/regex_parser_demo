def parse_regex(regex):
    output = []
    operators = []
    precedence = {'|': 1, '.': 2, '*': 3}
    
    def apply_operator():
        operator = operators.pop()
        if operator == '*':
            output.append('*')
        elif operator in {'|', '.'}:
            right = output.pop()
            left = output.pop()
            output.append((left, operator, right))

    for char in regex:
        if char.isalpha():
            output.append(char)
        elif char in precedence:
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[char]):
                apply_operator()
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators and operators[-1] != '(':
                apply_operator()
            operators.pop()

    while operators:
        apply_operator()

    return output[0]
