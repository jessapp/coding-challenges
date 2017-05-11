# Write an efficient function that checks whether any permutation of an input string is a palindrome.

def palindrome_permutation(string):

    letter_count = {}

    for letter in string:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    odd_count = 0

    for num in letter_count.values():
        if num % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False
    
    return True


print palindrome_permutation("ivicc")
print palindrome_permutation("livci")