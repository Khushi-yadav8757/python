Question:-Can a function be passed as an argument to another function?
          Yes. Functions are first-class objects.
Example-
def shout(text):
    return text.upper()

def greet(func):
    print(func("hello"))

greet(shout)
