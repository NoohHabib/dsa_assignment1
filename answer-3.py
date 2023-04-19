def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated = str1 + str1
    if str2 in concatenated:
        return True
    else:
        return False

# Example usage:
str1 = "abcd"
str2 = "cdab"
if are_rotations(str1, str2):
    print(str1, "and", str2, "are rotations of each other.")
else:
    print(str1, "and", str2, "are not rotations of each other.")
    