class MO:
    def myFunction(self, *args):
        if len(args) == 0:
            print("Function with no argument")
        elif len(args) == 1:
            print("Function with one argument")
        elif len(args) == 2:
            print("Function with two arguments")
        else:
            print("Function with too many arguments")

# Creating object
m = MO()
m.myFunction()
m.myFunction(10)
m.myFunction(10, 20)
