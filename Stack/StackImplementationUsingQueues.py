"""
Using two queues to implement stack with LIFO manner.
We use one queue1 and insert(enqueue) from the rear end to replicate push() functionality.
For pop() we dequeue() from queue1 and enqueue in q2 until queue is empty, then we do not enqueue the last element to replicate pop()
"""

from DS.Queues.Queue_using_array import *


class Stack_using_queues:

    peek_val = None
    @staticmethod
    def push(val):
        q1.enqueue(val)
        Stack_using_queues.peek_val = val

    @staticmethod
    def peek():
        print("Top at "+ str(Stack_using_queues.peek_val))

    @staticmethod
    def pop():
        last = True
        while last:
            val = q1.dequeue()
            l_data = val
            if q1.is_empty():
                print("Value popped " + str(l_data))
                last = False
            else:
                q2.enqueue(l_data)

        while not q2.is_empty():
            val = q2.dequeue()
            q1.enqueue(val)
            Stack_using_queues.peek_val = val

    @staticmethod
    def print_stack():
        q1.print_queue()



if __name__ == "__main__":
    q1 = ArrayQueue()
    q2 = ArrayQueue()
    s = Stack_using_queues()
    s.push(10)
    s.push(20)
    s.print_stack()
    s.pop()
    s.push(60)
    s.push(50)
    s.print_stack()
    s.peek()
    s.pop()
    s.print_stack()
    s.peek()