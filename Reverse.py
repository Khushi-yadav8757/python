#Reverse a string without using slicing
Ans:
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # put each character in front
    return reversed_str

print(reverse_string("hello"))  # Output: "olleh"
