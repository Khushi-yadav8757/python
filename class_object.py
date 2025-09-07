Q1. Write a class Car with attributes brand and color. Create an object and print them.
Ans:-

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Create object
car1 = Car("Toyota", "Red")
print(car1.brand)   # Toyota
print(car1.color)   # Red
