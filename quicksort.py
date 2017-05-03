def quick_sort(lst):

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