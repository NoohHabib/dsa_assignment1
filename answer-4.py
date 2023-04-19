def find_first_non_repeated_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string:
        if char_count[char] == 1:
            return char

    return None

# Example usage:
string = "abaccdeff"
first_non_repeated_char = find_first_non_repeated_char(string)
if first_non_repeated_char:
    print("The first non-repeated character in", string, "is:", first_non_repeated_char)
else:
    print("There are no non-repeated characters in", string)
    