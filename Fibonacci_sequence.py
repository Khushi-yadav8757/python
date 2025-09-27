#Fibonacci sequence (Recursion + Iteration)
#Recursion:
Ans:
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

print([fib_recursive(i) for i in range(6)])  
# Output: [0, 1, 1, 2, 3, 5]
