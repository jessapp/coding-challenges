"""Find all combinations of number in a given array that add up to a given number
>>> number_combinations([1, 2, 3, 4], 5)
[(1, 4), (2, 3)]

"""

def number_combinations(numbers, target):

    total_to_target = {}

    output = []

    for num in numbers:
        total_to_target[num] = (target - num)

    for num in numbers:
        if num in total_to_target.values():
            output.append(total_to_target[num], num)

    return output