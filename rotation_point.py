# Find index of rotation point in list of alphabetized words

def find_rotation_point(lst):

    first_word = lst[0]

    floor_index = 0

    ceiling_index = len(lst) - 1

    while floor_index < ceiling_index:

        guess = floor_index + ((ceiling_index - floor_index) / 2)
        print "guess", guess

        if lst[guess] >= first_word:
            floor_index = guess
            print "floor index", floor_index
        else:
            ceiling_index = guess
            print "ceiling index", ceiling_index


        if floor_index + 1 == ceiling_index:
            return ceiling_index


print find_rotation_point([4, 5, 6, 1, 2, 3])


print find_rotation_point([5, 1, 2, 3, 4])