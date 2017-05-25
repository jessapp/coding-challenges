# You can get to the top of a staircase by going up n steps
# You can go up 1, 2, or 3 steps at a time
# How many combinations of steps can you take to get to the top?

def count_steps(n):

    if n < 0:
        return 0

    elif n == 0:
        return 1

    else:
        return count_steps(n - 1) + (n - 2) + (n - 3)

print count_steps(3)