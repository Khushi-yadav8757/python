🔹 What is a List?

A list is a collection of items which is ordered, mutable (changeable), and allows duplicate values.
You can store different data types in a list.

🔹 How to Create a List

- A list of numbers
numbers = [1, 2, 3, 4, 5]

- A list of mixed data types
mixed = [10, "hello", 3.14, True]
     
- Empty list
empty = []

🔹 Accessing Elements in List (Indexing & Slicing)

fruits = ["apple", "banana", "mango", "orange"]

print(fruits[0])     # apple
print(fruits[-1])    # orange
print(fruits[1:3])   # ['banana', 'mango']

🔹 Modifying a List (Mutable)

fruits[1] = "grapes"
print(fruits)   # ['apple', 'grapes', 'mango', 'orange']

🔹 Useful List Methods

| Method           | Description                     |
| ---------------- | ------------------------------- |
| `append()`       | Adds an item at the end         |
| `insert(i, val)` | Inserts at index i              |
| `remove(val)`    | Removes first occurrence of val |
| `pop()`          | Removes last element            |
| `sort()`         | Sorts list in ascending order   |
| `reverse()`      | Reverses the list               |
| `clear()`        | Empties the list                |

nums = [3, 1, 4, 2]
nums.append(5)         # [3, 1, 4, 2, 5]
nums.sort()            # [1, 2, 3, 4, 5]
nums.pop()             # removes last item

 🔹 Loop Through List

for item in fruits:
    print(item)

🔹 Check if Item Exists

if "apple" in fruits:
    print("Yes, apple is in the list")

🔹 List Comprehension (Shortcut to make new lists)

squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
