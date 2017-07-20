#Given a sorted array consisting of only integers where every element appears 
#twice except for one element which appears once. Find this single element that 
# appears only once.

# Input: [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2

# def find_single(nums):

#     if nums[0] == nums[-1]:
#         return nums[0]

#     mid = len(nums) / 2

#     if mid % 2 == 0:

#         if nums[mid] == nums[mid + 1]:
#             return find_single(nums[mid + 1:])
#         else:
#             return find_single(nums[:mid])

#     else:
#         if nums[mid] == nums[mid - 1]:
#             return find_single(nums[mid + 1:])
#         else:
#             return find_single(nums[:mid - 1])


# print find_single([1, 1, 2, 4, 4, 5, 5, 6, 6])


def find_single(nums, low, high):
 
    # Base cases
    if low > high:
        return None
 
    if low == high:
        return nums[low]
 
    # Find the middle point
    mid = low + (high - low) / 2
 
    # If mid is even and element next to mid is
    # same as mid, then output element lies on the right

    if mid % 2 == 0:
 
        if nums[mid] == nums[mid + 1]:
            return find_single(nums, mid + 2, high)
        else:
            return find_single(nums, low, mid)
 
    # Otherwise, the element lies on the left side 
    else:
        # if mid is odd
        if nums[mid] == nums[mid - 1]:
            return find_single(nums, mid + 1, high)
        else:
            return find_single(nums, low, mid - 1)

nums = [ 1, 1, 2, 4, 4, 5, 5, 6, 6 ]
 
# Function call
print find_single(nums, 0, len(nums)-1)