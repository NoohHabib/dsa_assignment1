def are_brackets_closed(code):
    stack = []
    for char in code:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False
    return not stack

# Example usage:
code1 = "(a + b) * (c - d)"
code2 = "{[a + b] * (c - d)}"
code3 = "{(a + b) * (c - d]"
if are_brackets_closed(code1):
    print("Brackets are closed in code1")
else:
    print("Brackets are not closed in code1")
if are_brackets_closed(code2):
    print("Brackets are closed in code2")
else:
    print("Brackets are not closed in code2")
if are_brackets_closed(code3):
    print("Brackets are closed in code3")
else:
    print("Brackets are not closed in code3")
    