"""
Given a list of daily temperatures T, return a list such that, 
for each day in the input, tells you how many days you would have 
to wait until a warmer temperature. If there is no future day for 
which this is possible, put 0 instead.

For example, given the list of temperatures 
T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].
"""

def daily_temps(nums):
    # Initialize an empty list
    ret = [0] * len(nums)

    # Initialize a stack
    stack = []

    for i, v in enumerate(nums):
        # if there is a stack, we want to see which value is
        # lower - the current value or the last value in the 
        # stack.
        while stack and stack[-1][1] < v:
            index, value = stack.pop()
            ret[index] = i - index

        # Append to the stack no matter what - this is what fills
        # it out
        stack.append(i, v)

    return ret 