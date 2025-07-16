1. print() fuction 
print("Hello world")

2.round() function
x =round(53.6437846,2) #after point we get only 2 digit after use ,2.
print(x)
---------------------------------------------------------------------------
#Create function
def myfunction():
  print("hello")
myfunction()  #calling a function
---------------------------------------------------------------------
# function with one argument
#creating a function
def myfunction(a):
  print("A: ",a)
myfunction(10)  #pasing argument as 10
-----------------------------------------------------------------
#keyword argument
def myfunction(child3,child2,child1):
  print("Youngest child is :"+child3)
myfunction(child1="Ram",child2="nivi",child3="Shristi")  
-----------------------------------------------------------------
#Default parameter Value
def myfunction(state="bihar"):
  print("i am from "+state)
myfunction("Rajsthan")
myfunction("goa")
myfunction()
---------------------------------------------------------------------------
Passing a list into function
def myfunction(fruit):
  for i in fruit:
    print(i)
F=["Apple","Banana","Cherry","Date"] 
myfunction(F)
-------------------------------------------------------------------
#Recursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num = 6  # replace with int(input("Num:")) if you're running locally
print("The Factorial of", num, "is:", factorial(num))
----------------------------------------------------------------------------
