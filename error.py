try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Oops! File not found.")
