# Convert a python into into a binary number

class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self , item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

def int2bin(num):

    remstack = Stack()

    while num > 0:
        # Continuously divides the number by 2, and pushes the remainder onto the stack 
        # Even numbers will have a remainder of zero. Odd numbers will have a remainder of one
        rem = num % 2
        remstack.push(rem)

        # // is floor division - results in whole number adjusted to the left in the number line
        num = num // 2

    # Once the number has been divided down to zero
    binstring = ""

    # The binary digits are popped one at a time and appended to the right-hand side of the string
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())

    return binstring

print int2bin(13)
print int2bin(42)