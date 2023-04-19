def find_pairs(arr, target):
    pairs = []
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
target = 7
pairs = find_pairs(arr, target)
print("Pairs with sum", target, "are:", pairs)
