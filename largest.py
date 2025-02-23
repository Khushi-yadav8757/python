a=float(input("enter the first number :"))
b=float(input("enter the second number :"))
c=float(input("enter the third number :"))
if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
print(f"the largest number is:{largest}")            
