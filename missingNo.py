#Find Missing Number in a Sequence
Company Asked: Capgemini


def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)

print(find_missing_number([1, 2, 4, 5]))  # Output: 3
