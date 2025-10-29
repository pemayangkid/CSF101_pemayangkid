def lengthofLongestSubstrings(s):
    char_index = {}
    max_length = 0
    start = 0

    for end,char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, end - start + 1)

        char_index[char] = end

    return max_length
print(lengthofLongestSubstrings(["dbcghdbc"]))
print(lengthofLongestSubstrings(["abcbbbdg"]))