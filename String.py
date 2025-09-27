#Check if a string is a palindrome
Ans:
def is_palindrome(s):
    return s == s[::-1]  # compare with reversed string

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
