file = open("data.txt", "r")
print(file.read())          # Read full content
print(file.readline())      # Read one line
print(file.readlines())     # Returns list of lines
file.close()
