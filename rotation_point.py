# Find index of rotation point in list of alphabetized words

def find_rotation_point(lst):

    first_word = lst[0]

    floor_index = [0]

    ceiling_index = len(lst) - 1

    while floor_index < ceiling_index:

        guess = floor_index + ((ceiling_index - floor_index) / 2)

        if lst[guess] >= first_word:
            floor_index = guess
        else:
            ceiling_index = guess


        if floor_index + 1 == ceiling_index:
            return ceiling_index