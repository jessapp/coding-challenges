# Write a recursive function that multiplies two positive integers wihtout using the *
# Operator. 

def recursive_multiply(num1, num2, current_total=0):

    if num2 == 0:
        return current_total

    current_total += num1

    return recursive_multiply(num1, (num2 - 1), current_total)

print recursive_multiply(10, 10)