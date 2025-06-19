Tuple?
A tuple is a collection of items that is:
Ordered
Immutable (cannot be changed after creation)
Allows duplicate values

Defined using parentheses ()

Creating a Tuple
my_tuple = (10, 20, 30)
print(my_tuple)
Even a single-element tuple needs a comma:

python
Copy
Edit
single = (5,)
print(type(single))  # Output: <class 'tuple'>
Accessing Tuple Element
print(my_tuple[0])  # Output: 10
print(my_tuple[-1]) # Output: 30
 
Tuple vs List
Feature	List	Tuple
Syntax	[]	()
Mutable	Yes	No
Performance	Slower	Faster
Methods	Many	Fewer

Tuple Methods

Method	Description
count(x)	Returns number of times x appears
index(x)	Returns index of first occurrence of x

numbers = (1, 2, 3, 2, 4)
print(numbers.count(2))  # Output: 2
print(numbers.index(3))  # Output: 2

Tuple Packing and Unpacking

# Packing
person = ("Khushi", 21, "India")

# Unpacking

name, age, country = person
print(name)     # Khushi
print(age)      # 21
print(country)  # India

