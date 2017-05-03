# Write a function to reverse a string in-place.

def reverse_in_place(string):

    string_list = list(string)

    left = 0
    right = len(string_list) - 1

    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]

        left += 1
        right -= 1

    return ''.join(string_list)