Q2. Create a parent class Animal with method speak(). Create child class Dog that overrides speak().
Ans:- 

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

dog = Dog()
dog.speak()   # Woof! Woof!
