#Can you return multiple values from a Python function?
Yes,You can return multiple values using tuple:
Example-
def operations(a, b):
    return a+b, a-b, a*b
x, y, z = operations(10, 5)
print(x, y, z)
