def isanagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    character_counts = [0] * 26

    for c1, c2 in zip(s,t):
        character_counts[ord(c1) - ord('a')] += 1
        character_counts[ord(c2) - ord('a')] -= 1
    return all(count == 0 for count in character_counts)
print(isanagram([s=pema, t=aepm]))