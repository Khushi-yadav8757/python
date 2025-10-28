#Sort a dictionary by values

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))
    
my_dict = {"a": 3, "b": 1, "c": 2}
print(sort_dict_by_value(my_dict))
# Output: {'b': 1, 'c': 2, 'a': 3}
