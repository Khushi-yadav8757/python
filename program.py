✅ 1. Create a list of 5 cities and print them using a loop

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
for city in cities:
    print(city)

Output:
Delhi
Mumbai
Kolkata
Chennai
Bangalore

✅ 2. Write a program to add 10 to each element in a list using list comprehension
numbers = [5, 10, 15, 20, 25]

# Add 10 to each element
updated_numbers = [num + 10 for num in numbers]

print(updated_numbers)
Output:
[15, 20, 25, 30, 35]
✅ 3. Make a list of even numbers from 1 to 20

even_numbers = [num for num in range(1, 21) if num % 2 == 0]

print(even_numbers)
Output:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
