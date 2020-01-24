# Implement a queue with 2 stacks. 
# Your queue should have an enqueue and a dequeue function and it should be "first in first out" (FIFO).

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack

class Queue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        """Adds to the back of a queue"""
        self.stack1.push(item)

    def dequeue(self):
        """Removes from the front of the queue"""

        if self.stack2 is None:
            
            while self.stack1 is not None:
                item = self.stack1.pop()
                self.stack2.push(item)

            if len(self.stack2) == 0:
                raise IndexError

        return self.stack2.pop()

        