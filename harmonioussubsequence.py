# We define a harmonious array is an array where the difference between its 
# maximum value and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious 
# subsequence among all its possible subsequences.

def longest_harmonious_subsequence(nums):

    subs = []

    for i in range(len(nums)):
        for j in range(0, i):
            sub = nums[j: i + 1]

            if max(sub) - min(sub) == 1:
                subs.append(sub)

    longest = None
    max_len = 0

    for subsequence in subs:
        if len(subsequence) > max_len:
            longest = subsequence
            max_len = len(subsequence)


    return longest


print longest_harmonious_subsequence([1,3,2,2,5,2,3,7])