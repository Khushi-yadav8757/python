# Check if Two Lists Have Common Elements
#Company Asked: Infosys

def has_common_element(list1, list2):
    return bool(set(list1) & set(list2))

print(has_common_element([1, 2, 3], [4, 5, 2]))  # Output: True
