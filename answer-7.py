def is_operand(char):
    return char.isalpha() or char.isdigit()

def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in reversed(expression):
        if is_operand(char):
            stack.append(char)
        elif char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = '(' + operand1 + char + operand2 + ')'
            stack.append(infix)
    return stack.pop()

# Example usage:
expression = "*+AB-CD"
infix_expression = prefix_to_infix(expression)
print("Infix expression:", infix_expression)


