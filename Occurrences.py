Q.Count Occurrences of Each Character
Ans:
def char_count(s):
    from collections import Counter
    return Counter(s)

print(char_count("programming"))
