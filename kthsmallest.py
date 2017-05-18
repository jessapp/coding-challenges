# Given a list of numbers in random order write a linear time algorithm to find the 𝑘th
# smallest number in the list.

def sort_lst(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) / 2

    pivot = lst[mid]

    low, high, equal = [], [], []

    for num in lst:
        if num < pivot:
            low.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            high.append(num)

    return quick_sort(low) + equal + quick_sort(high)

sorted_lst = sort_lst(lst)

def kth_smallest(sorted_lst, k):

    index = k - 1

    return lst[index]

