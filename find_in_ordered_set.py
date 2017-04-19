#Suppose we had a list of n integers sorted in ascending order. How quickly could we check if a given integer is in the list?

def find_in_lst(lst, num):

    for item in lst:
        if item == num:
            return True
        if item < num:
            return False

# Runtime = O(n)
# Or, use binary search for O(log n)