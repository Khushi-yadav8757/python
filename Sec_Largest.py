#Find the second largest number in a list
Ans:
def second_largest(nums):
    unique_nums = list(set(nums))  # remove duplicates
    unique_nums.sort()
    return unique_nums[-2]  # second last element

print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
