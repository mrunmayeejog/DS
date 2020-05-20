"""
Using two stacks implement queue so as to replicate FIFO manner.
In stack1 push() elements similar to enqueue(). At the time of dequeue, pop() all elements from stack1 to stack2 and
pop() top value to replicate dequeue()
"""

from DS.Stack.Stack_using_Array import *


def dequeue():
    while not s1.is_empty():
        val = s1.pop()
        s2.push(val)
    val = s2.pop()
    print("\n Value dequeued is "+ str(val))

    while not s2.is_empty():
        val = s2.pop()
        s1.push(val)

def enqueue(val):
    s1.push(val)

def print_queue():
    s1.print_stack()


if __name__ == "__main__":
    s1 = Array_stack()
    s2 =Array_stack()
    enqueue(10)
    enqueue(20)
    enqueue(30)
    enqueue(40)
    enqueue(50)
    enqueue(60)
    print_queue()
    dequeue()
    print_queue()
    dequeue()
    print_queue()
