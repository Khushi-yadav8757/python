#Difference between deepcopy and copy
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)      # Shallow copy
c = copy.deepcopy(a)  # Deep copy
