def parse_regex(regex):
    output = []
    operators = []
    precedence = {'|': 1, '.': 2, '*': 3}

    def apply_operator():
        operator = operators.pop()
        if operator == '*':
            operand = output.pop()
            output.append((operand, '*'))
        elif operator in {'|', '.'}:
            right = output.pop()
            left = output.pop()
            output.append((left, operator, right))

    for i, char in enumerate(regex):
        if char.isalpha():
            output.append(char)
            if i + 1 < len(regex) and (regex[i + 1].isalpha() or regex[i + 1] == '('):
                while operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence['.']:
                    apply_operator()
                operators.append('.')
        elif char == '(':
            operators.append(char)
            if i + 1 < len(regex) and (regex[i + 1].isalpha() or regex[i + 1] == '('):
                while operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence['.']:
                    apply_operator()
                operators.append('.')
        elif char == ')':
            while operators and operators[-1] != '(':
                apply_operator()
            operators.pop() 
        elif char in precedence:
            while operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence[char]:
                apply_operator()
            operators.append(char)

    while operators:
        apply_operator()

    return output
