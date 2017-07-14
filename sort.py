# Sort an array of positive integers of the size N where all ints are all less than N 
# This can be done in O(n) runtime

def sort(nums, n):

    if len(nums) <= 1:
        return nums

    counter = [0] * n 

    for num in nums:
        counter[num] += 1

    final_array = []

    for lst_index, num in enumerate(counter):
        for i in range(num):
            final_array.append(lst_index)

    return final_array

print sort([2, 3, 1, 8, 4, 2], 9)

print sort([4], 5)