🔶 Intermediate Python Questions
🔸 11. What is the difference between deep copy and shallow copy?
Answer:

Shallow copy creates a new object but references the same nested objects.

Deep copy creates a new object and recursively copies all nested objects.

python
Copy
Edit
import copy

lst = [[1, 2], [3, 4]]
shallow = copy.copy(lst)
deep = copy.deepcopy(lst)
🔸 12. What are Python lambda functions?
Answer:
Lambda functions are anonymous functions defined using the lambda keyword.

python
Copy
Edit
square = lambda x: x * x
print(square(5))  # Output: 25
🔸 13. Explain map(), filter(), and reduce() functions.
Function	Purpose	Example
map()	Applies a function to each item	map(lambda x: x*2, [1,2,3])
filter()	Filters items based on condition	filter(lambda x: x%2==0, [1,2,3,4])
reduce()	Applies rolling computation	reduce(lambda x,y: x+y, [1,2,3])

reduce() must be imported from functools.

🔶 OOP in Python Interview Questions
🔸 14. What is OOP in Python?
Answer:
Object-Oriented Programming is a paradigm that uses objects and classes to model real-world entities.

Key concepts:

Class

Object

Inheritance

Encapsulation

Polymorphism

🔸 15. Write a basic class in Python.
python
Copy
Edit
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

p = Person("Khushi")
p.greet()  # Output: Hello, I am Khushi
