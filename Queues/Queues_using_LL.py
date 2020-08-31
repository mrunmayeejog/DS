"""
Implementing queues using Linkedlists.
Enqueue or insert at tail/rear end and Dequeue/delete from front end.
"""


class queue_node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queues_using_LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def front(self):
        if self.head:
            # print("Front at " + str(self.head.data))
            return True
        else:
            # print("Queue is empty")
            return False

    def rear(self):
        if self.tail:
            print("Rear at " + str(self.rear.data))
            return
        print("Queue is empty")

    def isempty(self):
        if not self.head:
            return True
        return False

    def enqueue(self, val):
        new_node = queue_node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        curr = self.tail
        curr.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            # print("Queue is empty")
            return
        val = self.head.data
        self.head = self.head.next
        return val

    def print_queue(self):
        if self.head == None:
            print("Queue is empty")
            return
        curr = self.head
        while curr:
            print(" " +str(curr.data) + " ", end ="")
            curr = curr.next
        print("\n")


if __name__ == "__main__":
    q = Queues_using_LL()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.enqueue(77)
    q.print_queue()