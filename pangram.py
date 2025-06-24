# Check Pangram
Company Asked: Cognizant
A pangram is a sentence that contains every letter of the alphabet.



import string

def is_pangram(sentence):
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
