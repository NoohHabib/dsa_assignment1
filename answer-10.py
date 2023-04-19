def find_smallest_number(stack):
    if not stack:
        return None
    smallest = stack.pop()
    if not stack:
        return smallest
    else:
        temp = find_smallest_number(stack)
        if smallest < temp:
            return smallest
        else:
            return temp

# Example usage:
stack = [5, 2, 9, 1, 7]
smallest = find_smallest_number(stack)
if smallest:
    print("The smallest number in the stack is:", smallest)
else:
    print("The stack is empty.")
    