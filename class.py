class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Object banaye
s1 = Student("Khushi", 101)
s1.display()
