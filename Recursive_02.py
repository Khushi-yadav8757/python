def sum_recursive(n):
    if n==0:
      return 0
    return n + sum_recursive(n-1)
result = sum_recursive(10)
print("Sum from 0 to 10: ",result)      
