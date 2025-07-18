#Check Armstrong Number
#Company Asked: Wipro

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n

print(is_armstrong(153))  # Output: True
