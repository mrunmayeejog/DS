"""
Queues data structure that works in FIFO manner. Queue consists of standard APIs such as enqueue() to insert new data at
the rear end and dequeue operation to remove from the front end. Queues can be implemented with arrays as well as linkedlists.
In case of arrays, we use Array as an ADT and use append and delete functions.
With Queues using linked lists we maintain another pointer as tail which helps in inserting at tail/rear end and we delete at head.
"""
Max = 50

class ArrayQueue:

    def __init__(self):
        self.data = Max * [None]
        self.size = 0
        self.front = 0

    def length(self):
        return self.size

    def print_queue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        for i in range(0, len(self.data)):
            if self.data[i]:
                print((' ' + str(self.data[i])), end=' ')
        print("\n")

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == Max

    def enqueue(self, value):
        if self.is_full():
            # print("Queue is full can not add value " + str(value))
            return
        self.data[self.size] = value
        self.size += 1

    def sort_array(self):
        for i in range(0, len(self.data)):
            if self.data[i] == None:
                self.data.pop(i)
                self.data.append(None)

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        val = self.data[0]
        self.data[0] = None
        self.size -= 1
        self.sort_array()
        return val

    def first(self):
        if self.is_empty():
            return
        return self.data[self.front]


if __name__ == '__main__':
    q = ArrayQueue()
    for i in range(1, 6):
        q.enqueue(i)
    q.print_queue()
    q.dequeue()
    q.print_queue()
    print(q.length())