#Count frequency of elements in a list
Ans:
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq
    
print(count_frequency([1, 2, 2, 3, 1, 4, 2]))
# Output: {1: 2, 2: 3, 3: 1, 4: 1}
