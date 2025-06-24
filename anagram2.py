# Check for Anagram Strings
#Company Asked: TCS
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram("listen", "silent"))  # Output: True
