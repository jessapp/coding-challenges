#Given a list of unsorted numbers and an integer (n), return the n biggest and n 
#smallest elements from that list of numbers. 


def minmax(nums, n):

    if len(nums) < n:
        return None

    copy = nums[:]

    biggest = []

    smallest = []

    for i in range(n):
        biggest.append(max(copy))
        smallest.append(min(copy))
        copy.remove(max(copy))
        copy.remove(min(copy))


    return (biggest, smallest)

print minmax([22, 6, 42, 9, 10, 23, 5, 1, 8], 3)