# Given a collection of distinct integers, return all possible permutations.

def get_permutations(nums):
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        # Wrapping this in a list is integral to the recursion
        return [nums]

    all_perms = []

    for i in range(len(nums)):
        current_num = nums[i]
        list_without_current = nums[:i] + nums[i+1:]

        for perm in get_permutations(list_without_current):
            all_perms.append([current_num] + perm)

    return all_perms