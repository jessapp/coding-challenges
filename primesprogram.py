from sys import exit


def start():
    """Starts the program"""

    print "Enter an integer number of primes to generate."
    print "Type quit to exit the program"

    choice = raw_input("Primes> ")

    if choice == "quit":
        print "Bye!"
        exit()

    elif choice.isdigit():
        primes(choice)

    else:
        print "Invalid input"
        start()



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

    print "Primes: ", prime_nums


start()