✅ 1. Create a tuple of 5 colors and print them using a loop
colors = ("red", "blue", "green", "yellow", "pink")

for color in colors:
    print(color)
Output:
red
blue
green
yellow
pink

✅ 2. Create a tuple of marks and count how many times 90 appears

marks = (90, 85, 90, 76, 90)
count_90 = marks.count(90)
print("90 appears", count_90, "times.")
Output:
90 appears 3 times.

✅ 3. Try to change an element in a tuple and observe the error

numbers = (10, 20, 30)
numbers[0] = 100    # ❌ This will cause an error
Error:
php
TypeError: 'tuple' object does not support item assignment
➡️ This error proves that tuples are immutable (you cannot change their content after creation).

