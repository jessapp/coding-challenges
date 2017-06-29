# Given an array of integers and a target, return all unique triplets that equal the target

def threesum(nums, target):

    if len(nums) < 3:
        return []

    nums.sort()

    final = set()

    # going over every index, except the last one
    for i in range(0, len(nums) - 2):

        # set a second index, right after the first
        second_index = i + 1

        # and a third index, which is the last index in the list
        third_index = len(nums) - 1

        # While the second index is less than the third index
        # And the second index is greater than the first index
        while second_index < third_index and second_index > i:
            # Add all three together 
            total = nums[i] + nums[second_index] + nums[third_index]

            # if the total adds up the target, add it to the set, and
            # increase the second index
            if total == target:
                a = (nums[i], nums[second_index], nums[third_index])
                final.add(a)
                second_index += 1

            # If the total is greater than the target, move back the final index
            elif total > target:
                third_index -= 1

            # otherwise, increase the second index
            else:
                second_index += 1

    return list(final)


print threesum([1, 2, 5, 2, 6, 7, 4, 8], 9)
