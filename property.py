#Explain property() and @property.
Ans:
Used to define getters/setters in a Pythonic way.
------------------------------------------------
class Person:
    def __init__(self, name):
        self._name = name
--------------------------------
    @property
    def name(self):
        return self._name
