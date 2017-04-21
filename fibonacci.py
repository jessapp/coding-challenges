# Write a function fib() that a takes an integer n and returns the nth fibonacci number.


# recursive solution, O(2^n) runtime
# def fib(n):

#     fib_nums = [0, 1]

#     if n in fib_nums:
#         return n

#     return fib(n-1) + fib(n-2)


# print fib(7)

#iterative soultion: 

def fib_iterative(n):

    if n < 0:
        raise Exception('Negative number')


    if n in [1, 0]:
        return n

    first_num = 0
    second_num = 1

    for i in range(n - 1):
        current = first_num + second_num
        first_num = second_num
        second_num = current

    return current

