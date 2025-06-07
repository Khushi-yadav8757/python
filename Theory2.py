🔹 6. What is a dictionary in Python?
Answer:
A dictionary is an unordered collection of key-value pairs.


student = {"name": "Khushi", "age": 21}
print(student["name"])  # Output: Khushi
🔹 7. What are functions in Python?
Answer:
A function is a reusable block of code that performs a specific task.


def greet(name):
    return "Hello " + name

print(greet("Khushi"))
🔹 8. What is the difference between append() and extend() in a list?
Answer:

append() adds one element to the end.

extend() adds multiple elements from another iterable.

lst = [1, 2]
lst.append([3, 4])  # [1, 2, [3, 4]]
lst.extend([5, 6])  # [1, 2, [3, 4], 5, 6]
🔹 9. **What are *args and kwargs?
Answer:

*args allows passing a variable number of positional arguments.

**kwargs allows passing a variable number of keyword arguments.

def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, name="Khushi", age=21)
🔹 10. What is list comprehension?
Answer:
It is a concise way to create lists.

squares = [x*x for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
