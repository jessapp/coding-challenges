# You have a function rand7() that generates a random integer from 1 to 7. Use it to
# write a function rand5() that generates a random integer from 1 to 5.

def rand5():

    result = 7

    while result > 5:
        result = rand7()

    return result

