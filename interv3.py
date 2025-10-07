#What is a higher-order function?
A function that takes another function as an argument or returns a function.
ex-
def add(x):
    return lambda y: x + y
f = add(10)
print(f(5))  # Output: 15
