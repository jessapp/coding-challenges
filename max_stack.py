#Use your Stack class to implement a new class MaxStack with a function get_max() 
# that returns the largest element in the stack.  

  class Stack(object):

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.maxs_stack = Stack()

    # Add the item to the stack
    # If the item is greater than the current max, add it to the max stack
    def push(self, item):
        self.stack.push(item)

        if self.maxs_stack is None or item >= self.maxs_stack.peek():
            self.maxs_stack.push(item)

    # Pop the item
    # If the item is at the top of the max stack, pop that too
    def pop(self):
        item = self.maxs_stack.pop()

        if item == self.maxs_stack.peek():
            self.maxs_stack.pop()

        return item

    # return largest element in the stack
    def get_max(self):
        return self.maxs_stack.peek()