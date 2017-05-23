# Bubble sort

def bubble_sort(nums):

    for i in rage(len(nums) - 1):

        made_swap = False

        for j in range(len(nums) - 1 - i):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                made_swap = True

        if not made_swap:
            break


# Merge sort

def merge_sort(nums):
    # breaks everything down into a list of 1

    if len(nums) < 2:
        return lst

    mid = len(nums) / 2

    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return make_merge(lst1, lst2)

def make_merge(lst1, lst2):

    final_list = []

    while len(lst1) > 0 or len(lst2) > 0:

        if lst1 == []:
            final_list.append(lst2.pop(0))

        elif lst2 == []:
            final_list.append(lst1.pop(0))

        elif lst1[0] < lst2[0]:
            final_list.append(lst1.pop(0))
        else:
            final_list.append(lst2.pop(0))

    return final_list


# Quicksort 

def quicksort(nums):

    if len(nums) < 2:
        return nums

    mid = len(nums) / 2

    pivot = nums[mid]

    lower = []
    equal = []
    higher = []

    for num in nums:
        if num < pivot:
            lower.append(num)
        elif num > pivot:
            higher.append(num)
        else:
            equal.append(num)

    return quicksort(lower) + equal + quicksort(higher)

