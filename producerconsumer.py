# Implement a solution to producer_consumer problem

import random

queue = []

max_length = 10

class Producer(object):

    def __init__(self):
        pass

    def start(self):

        if len(queue) < max_length:
            new_num = random.randint(1, 10)
            queue.append(new_num)
            print "Produced %s" % new_num

class Consumer(object):

    def __init__(self):
        pass

    def start(self):

        if len(queue) > 0:
            output = queue.pop(0)
            print "Consumed %s" % output
        else:
            print "Queue empty, cannot consume"


def producer_consumer_problem():

    while queue:
        Producer.start()
        Consumer.start()