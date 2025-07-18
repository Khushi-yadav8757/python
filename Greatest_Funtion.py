# WAP using function to find the greatest of three numbers
def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = 68
b = 90
c = 78

print(greatest(a, b, c))
