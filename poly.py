class Bird:
    def sound(self):
        print("Chirp")

class Duck(Bird):
    def sound(self):
        print("Quack")

b = Bird()
d = Duck()
b.sound()  # Chirp
d.sound()  # Quack
