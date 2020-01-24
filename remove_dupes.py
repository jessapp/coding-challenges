# Remove duplicates from a sorted array without creating a new array.
# Return the length of the arrray without duplicates

def remove_dupes(arr):
    if len(arr) <= 1:
        return len(arr)

    current_index = 0

    # We do -1 because we always check the next index. 
    # Would cause and index error otherwise
    while current_index < (len(arr) - 1):
        if arr[current_index] == arr[current_index + 1]:
            arr.pop(current_index)
            # need to backtrack the index
            current_index -= 1
        current_index += 1

    return len(arr)
