from sys import exit
import argparse

def is_prime(num):
    """Helper function to check if a number is prime"""

    if num < 2:
        return False

    for i in range (2, (num /2 ) + 1):
        if num % i == 0:
            return False

    return True

def primes(count):
    """Finds sequence of prime numbers"""

    prime_nums = []

    num = 2

    total = int(count)

    while total > 0:

        if is_prime(num):
            prime_nums.append(num)
            total -= 1

        num += 1

    return prime_nums


parser = argparse.ArgumentParser(description='Find a certain number of primes')

parser.add_argument('-n', '--num_primes', help="choose how many primes to display", type=int)
parser.add_argument('-o', '--output', help="output to a .txt file")

args = parser.parse_args()

answer = primes(args.num_primes)

if not args.output:
    print answer
else:
    text_file = open(str(args.output), "w")
    text_file.write(str(answer))
    text_file.close()