# Given a non-negative integer num, repeatedly add all its digits until the 
#result has only one digit.

# For example:

# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only 
#one digit, return it.


def digital_sum(num):

    total = 0

    for i in str(num):
        total += int(i)

    return total


def digital_root(num):

    result = digital_sum(num)

    if result < 10:
        return result
    else:
        return digital_root(result)

print digital_root(12345)