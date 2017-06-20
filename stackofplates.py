# Imagine a literal stack of plates - at a certain time, it would get too high and topple over
# At that point, you'd need to make a new stack
# Implement a data structure SetOfStacks that mimics this behavior 

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):

        return self.stack.pop()

    def peek(self):

        return self.stack[-1]

class SetOfStacks(self):

    def __init__(self, maximum_value):
        self.stacks = []
        self.maximum_value = maximum_value

    def push(self, item):

        # If there are no stacks, initialize one and push onto it

        if self.stacks == []:
            new_stack = Stack()
            new_stack.push(item)
            self.stacks.append(new_stack)

        # Otherwise, check to see if the most recent stack is full
        # If it isn't, push onto it
        # If it is, create a new stack
        else:
            current_stack = self.stacks[-1]

            if len(current_stack) < self.maximum_value:
                current_stack.push(item)
            else:
                new_stack = Stack()
                new_stack.push(item)
                self.stacks.append(new_stack)

    def pop(self):

        # If there is nothing to pop, return None
        if self.stacks == []:
            return None
        # Otherwise, check the most recent stack and return the last item in it    
        else:
            current_stack = self.stacks[-1]
            item = current_stack.pop()

            # If popping that item leaves nothing in the stack, remove that stack from the list of stacks
            if len(current_stack) == 0:
                self.stacks.pop()

            return item

