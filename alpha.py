#Sort Words Alphabetically from a Sentence
#Company Asked: Accenture

def sort_words(sentence):
    words = sentence.split()
    words.sort()
    return " ".join(words)

print(sort_words("python is very easy to learn"))  
# Output: easy is learn python to very
