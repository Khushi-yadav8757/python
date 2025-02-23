a=int(input("enter a number :"))

factorial=1
if a<0:
    print("factorial is not defined for negative numbers.")
else:
    for i in range(1,a+1) :
        factorial*=i
    print(f"the factorial of {a} is {factorial}")    
