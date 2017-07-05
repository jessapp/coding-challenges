# Given a binary array, find the maximum number of consecutive 1s in this array

def consecutive_ones(nums):

    max_count = 0

    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

print consecutive_ones([1, 1, 0, 1, 1, 1])