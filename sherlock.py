# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string txt, determine if it is valid. If so, return "YES", otherwise return "NO".

# For example, If txt = "abc", the string is valid because the frequencies of characters are all the same. If txt = "abcc", the string is also valid, because we can remove 1 "c" and have one of each character remaining in the string. However, if txt = "abccc", the string is not valid, because removing one character does not result in the same frequency of characters.

# Examples
# is_valid("aabbcd") ➞ "NO"
# # We would need to remove two characters, both c and d  -> aabb or a and b -> abcd, to make it valid.
# # We are limited to removing only one character, so it is invalid.

# is_valid("aabbccddeefghi") ➞ "NO"
# # Frequency counts for the letters are as follows:
# # {"a": 2, "b": 2, "c": 2, "d": 2, "e": 2, "f": 1, "g": 1, "h": 1, "i": 1}
# # There are two ways to make the valid string:
# # Remove 4 characters with a frequency of 1: {f, g, h, i}.
# # Remove 5 characters of frequency 2: {a, b, c, d, e}.
# # Neither of these is an option.

# is_valid("abcdefghhgfedecba") ➞ "YES"
# # All characters occur twice except for e which occurs 3 times.
# # We can delete one instance of e to have a valid string.

def is_valid(txt):
    counts = dict()
    freqs = dict()
    # split chars into words
    chars = [*txt]

    # get counts of characters
    for char in chars:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print(counts)
    
    # get frequency of counts
    for count in counts:
        if counts[count] in freqs:
            freqs[counts[count]] += 1
        else:
            freqs[counts[count]] = 1
    print(freqs)

    # check if there is only 1 or 2 frequencies, and how much they differ
    if (len(freqs) > 2):
        return ("NO")
    elif (len(freqs) == 1):
        return ("Yes")
    elif (list(freqs.items())[0][1] >= 2 and list(freqs.items())[1][1] >= 2):
        return ("NO")
        # pass
    elif (abs(list(freqs.keys())[0] - list(freqs.keys())[1]) >= 2):
        return ("NO")
        # pass
    else:
        return ("YES")


# print(is_valid("aabbccddeefghi"))#, "NO")
# print(is_valid("aabbcd"))#, "NO")
# print(is_valid("abcdefghhgfedecba"))#, "YES")
# print(is_valid("abc"))#, "YES")
# print(is_valid("abcc"))#, "YES")
# print(is_valid("abccc"))#, "NO")