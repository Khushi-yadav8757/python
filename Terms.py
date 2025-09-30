#Explain @staticmethod, @classmethod, and instance methods.
Ans:
Instance method → takes self, works with object data.

Class method → takes cls, works with class-level data.

Static method → no self/cls, behaves like a normal function inside class.

class MyClass:
    def instance_method(self):
        return "instance"

    @classmethod
    def class_method(cls):
        return "class"

    @staticmethod
    def static_method():
        return "static"
