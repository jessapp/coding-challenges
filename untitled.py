class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        return self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack

def sort_stack(stack):

    temporary_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not temporary_stack.is_empty() and temporary_stack.peek() > temp:
            stack.push(temporary_stack.pop())

        temporary_stack.push(temp)

    while not temporary_stack.is_empty():
        stack.push(temporary_stack.pop())

    return stack 