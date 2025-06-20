-What is the scope of a variable in Python functions?
Local: Defined inside a function
Global: Defined outside any function
Ex--
x = 10  # global

def func():
    x = 5  # local
    print(x)
