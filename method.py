Q5.Show method overloading (using default arguments).
Ans:-

class MathOps:
    def add(self, a, b=0, c=0):
        return a + b + c

m = MathOps()
print(m.add(5))       # 5
print(m.add(5, 10))   # 15
print(m.add(5, 10, 20))  # 35
