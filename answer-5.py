def hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 discs from source to auxiliary peg
        hanoi(n - 1, source, target, auxiliary)

        # Move the nth disc from source to target peg
        print("Move disc", n, "from", source, "to", target)

        # Move the n-1 discs from auxiliary to target peg
        hanoi(n - 1, auxiliary, source, target)

# Example usage:
n = 3
hanoi(n, "A", "B", "C")
