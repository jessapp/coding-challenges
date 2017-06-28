# Given a digit, return all possible letter combinations that the number 
# on an old phone keyboard could represent.

# For example: 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

def letter_combinations(number_string):

    number_map = {'1': '',
                  '2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'   
                }

    if len(number_string) == 0:
        return []

    if len(number_string) == 1:
        return number_map[number_string]


    all_digits_but_last = number_string[:-1]
    combinations = letter_combinations(all_digits_but_last)

    last = number_string[-1]
    last_letters = number_map[last]

    strings = []

    for letter in last_letters:
        if len(combinations) != 0:
            for combo in combinations:
                new = combo + letter
                strings.append(new)
        else:
            strings.append(letter)

    return strings


print letter_combinations("833")
