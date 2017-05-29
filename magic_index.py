# Find magic index recursively

def magic_index(lst, start, end):

    if end < start:
        return None

    mid = len(lst) / 2

    midpoint = lst[mid]

    if mid == midpoint:
        return mid

    magic_index(lst[:mid], start, mid)

    magic_index(lst[mid + 1:], mid + 1, end)

    return None