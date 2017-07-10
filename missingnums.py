# Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

#Find all the elements of [1, n] inclusive that do not appear in this array.


def find_missing_nums(nums, n):

    expected_nums = set()

    for i in range(1, n+1):
        expected_nums.add(i)

    return expected_nums - set(nums)


print find_missing_nums([4, 3, 2, 7, 8, 2, 3, 1], 8)