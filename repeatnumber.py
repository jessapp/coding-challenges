# I have a list where every number in the range 1...n appears once except for one 
# number which appears twice.
# Write a function for finding the number that appears twice.


def repeat(lst, n):

    # counts = {}

    # for num in lst:
    #     counts[num] = counts.get(num, 0) + 1

    # for num, count in counts.items():
    #     if count == 2:
    #         return num

    sum_all_nums = ((n ** 2) + n) / 2

    sum_input_list = 