# Write a recursive function for generating all permutations of an input string. Return them as a set.

def recursive_permutations(string):

    if len(string) <= 1:
        return set(string)

    all_chars_except_last = string[:-1]
    print "all chars", all_chars_except_last
    last_char = string[-1]
    print "last char", last_char

    permutations_of_all_chars_except_last = recursive_permutations(all_chars_except_last)
    print "recurse", permutations_of_all_chars_except_last

    permutations = set()

    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            permutations.add(permutation)
            print "perm", permutation

    return permutations

print recursive_permutations("cats")