#File Open  – open() function

file = open("example.txt", "w")  # w = write mode
-----------------------------------------------
#Writing to a File – write()

Writing to a File – write()
-----------------------------------------------------
# Reading a File – read()

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
---------------------------------------------------
#Read Line by Line – readline()

file = open("example.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()
--------------------------------------------------------
#Reading All Lines in a Loop

file = open("example.txt", "r")
for line in file:
    print(line.strip())  # strip() removes new line
file.close()
--------------------------------------------------------
# Append to a File – a mode
file = open("example.txt", "a")
file.write("\nThis is new appended text.")
file.close()
-------------------------------------------------------
#Using with Keyword
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#here file.close automatially
---------------------------------------------------------
#Writing a List to File
fruits = ["Apple", "Banana", "Mango"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")
-----------------------------------------------------
#Reading List from File
with open("fruits.txt", "r") as file:
    fruits = [line.strip() for line in file.readlines()]

print(fruits)
---------------------------------------------------------
