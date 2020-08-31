"""
Circular queue using array. In circular queue, increment tail and insert/enqueue at tail. Dequeue from front or head.
"""

Max = 100


class CircularQueue:
    def __init__(self):
        self.tail = -1
        self.head = -1
        self.queue = [None] * Max
        self.len = 0

    def enqueue(self, val):
        if self.len == Max:
            print("Queue is full")
            return

        self.tail = (self.tail + 1) % Max
        self.queue[self.tail] = val
        self.len += 1

    def front(self):
        if self.tail == self.head == -1:
            print("Queue is empty")
            return
        print(self.queue[self.head])

    def rear(self):
        if self.tail == self.head == -1:
            print("Queue is empty")
            return
        print(self.queue[self.tail])

    def dequeue(self):
        if self.tail == self.head == -1:
            print("Queue is empty")
            return
        self.head = (self.head + 1) % Max
        self.len -= 1

    def print_queue(self):
        c = self.head
        i = 0
        while i < self.len:
            c = (c + 1) % Max
            if self.queue[c]:
                print(" " + str(self.queue[c]), end = " ")
            i += 1
        print("\n")


if __name__ == "__main__":
    c = CircularQueue()
    c.enqueue(10)
    c.enqueue(20)
    c.enqueue(30)
    c.print_queue()
    c.enqueue(40)
    c.enqueue(50)
    c.enqueue(60)
    c.enqueue(70)
    c.print_queue()
    c.dequeue()
    c.dequeue()
    c.dequeue()
    c.print_queue()