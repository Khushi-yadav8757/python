#Read CSV File (using just open)

with open("data.csv", "r") as f:
    for line in f:
        data = line.strip().split(",")
        print(data)
