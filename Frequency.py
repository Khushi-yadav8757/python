#Count Frequency of Elements in a List( Infosys)
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(count_frequency([1, 2, 2, 3, 3, 3]))  
# Output: {1: 1, 2: 2, 3: 3}
