-What is recursion in Python?
A function calling itself.
  Example-
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
