🟩 2. Tuples in Python
🔹 What is a Tuple?
A tuple is similar to a list, but it is:

✅ Ordered
❌ Immutable (you cannot change, add, or delete items)
✅ Allows duplicate values

Tuples are faster than lists and are used when your data should not be changed.

🔹 How to Create a Tuple
# Simple tuple
my_tuple = (10, 20, 30)

# Mixed data types
mixed = (1, "hello", 3.14)

# Single element tuple (Note the comma!)
single = (5,)  

# Empty tuple
empty = ()

🔹 Accessing Tuple Elements
numbers = (100, 200, 300)
print(numbers[0])     # 100
print(numbers[-1])    # 300

🔹 Tuple is Immutable (Can’t change elements)
t = (1, 2, 3)
# t[0] = 10  ❌ This will give an error

🔹 Tuple Operations
Operation	Description
len(t)	Returns length
t.count(val)	Count occurrences of a value
t.index(val)	Get the index of a value
for item in t:	Loop through a tuple

t = (1, 2, 3, 2, 4)
print(len(t))          # 5
print(t.count(2))      # 2
print(t.index(3))      # 2

🔹 Tuple Unpacking
person = ("Alice", 25, "Engineer")

name, age, profession = person

print(name)       # Alice
print(age)        # 25
print(profession) # Engineer

