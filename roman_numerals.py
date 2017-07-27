# Given a roman numeral, convert it to an integer

def roman_to_int(roman_num):

    roman = {'M': 1000, 
             'D': 500, 
             'C': 100, 
             'L': 50,
             'X': 10
             'V': 5
             'I': 1}


    total = 0

    # If one letter is less than it's latter one, the letter is subtracted
    for i in range(len(roman_num) - 1):
        if roman_num[roman_num[i]] < roman[roman_num[i + 1]]:
            total -= roman[roman_num[i]]
        
        # Otherwise, it's added
        else:
            total += roman[roman_num[i]]

    # The last letter is always added 
    return total + roman[roman_num[-1]]