# Write a function for doing an in-place shuffle of a list.

import random

def get_random(floor, ceiling):

    return random.randrange(floor, ceiling + 1)

def in_place_shuffle(lst):

    # Base case  - if the list is too small, return it 
    if len(lst) <= 1:
        return lst

    last_index = len(lst) - 1


    # For each index in the range of the list
    for index in range(0, last_index):

        # get a random index
        random_index = get_random(index, last_index)

        # if the index != the random index, swap them
        if random_index != index:

            lst[index], lst[random_index] = last_index[random_index], lst[index]