"""We have a reservoir of numbers or range of numbers in [a,b]. 
Write a Program that will return the minimum of the numbers out of the 
reservoir and remove that very number from the reservoir. At any point of time, 
values that were queried and taken off from the reservoir might be put back 
to the reservoir."""


class min_reservoir(object):

    def __init__(self):
        self.stack = []
        self.min_reservoir = []

    def push(self, item):
        self.stack.append(item)


        # If the minimum reservoir is currently empty, or if this item is larger
        # smaller than the current min, append it
        if self.min_reservoir is None or item <= self.min_reservoir[-1]:
            self.min_reservoir.append(item)

    def pop(self):
        if self.stack == []:
            return None
        
        # Pop the item from the stack.
        item = self.stack.pop()

        # If that is also the current minimum value, pop that as well
        if item == self.min_reservoir[-1]:
            self.min_reservoir.pop()


    def remove_min(self):

        num = self.min_reservoir.pop()

        self.stack.remove(num)

        return num

