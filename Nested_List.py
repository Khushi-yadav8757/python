#Flatten a nested list
Ans:
def flatten(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat

print(flatten([[1, 2], [3, 4], [5, 6]]))  
# Output: [1, 2, 3, 4, 5, 6]
