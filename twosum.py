# Given a list of unique numbers and a target, return indices of the two numbers such 
# that they add up to a specific target.

def two_sum(nums, target):

    index_and_num = {}

    for index, num in enumerate(nums):
        index_and_num[num] = index
        
        complement = target - num
        if complement in index_and_num:
            return [index_and_num[num], index_and_num[complement]]

    raise Exception("No two numbers add up to the target")


print two_sum([1, 2, 3, 4], 7)