"""
Circular linkedlist has all nodes pointing to the next with the last one pointing the next.
Except the last node points to the head. Does check the condition when next is head in loops.
"""

class cll_node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        newnode = cll_node(val)
        if not self.head:
            self.head = newnode
            newnode.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = newnode
        newnode.next = self.head
        self.head = newnode
        print(self.head.next.data)


    def insert_at_end(self, val):
        newnode = cll_node(val)
        if not self.head:
            self.head = newnode
            newnode.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = newnode
        newnode.next = self.head

    def insert_at_pos(self, pos, val):
        if pos == 0:
            self.insert_at_head(val)
        else:
            newnode = cll_node(val)
            curr = self.head
            i = 1
            while i < pos:
                if curr and curr.next != self.head:
                    curr = curr.next
                    i += 1
                else:
                    print("Invalid position ")
                    return

            newnode.next = curr.next
            curr.next = newnode
            print('New value ' + str(val) + ' inserted at position ' + str(pos))

    def delete_by_pos(self, pos):
        if not self.head:
            print("List is empty")
            return
        else:
            i = 0
            curr = self.head
            while i < pos:
                if curr and curr.next != self.head:
                    prev = curr
                    curr = curr.next
                    i += 1
                else:
                    print("Invalid position")
                    return
            prev.next = curr.next
            return

    def delete_by_val(self, val):
        if not self.head:
            print("List is empty")
            return
        else:
            curr = self.head
            prev = None
            found = False
            while curr.next != self.head:
                if curr.data == val:
                    found = True
                    break
                prev = curr
                curr = curr.next
            if found:
                prev.next = curr.next
                return
            else:
                print("invalid value")


    def print_ll(self):
        if not self.head:
            print("List is empty")
            return
        print('\nList contains:', end=' ')
        curr = self.head
        while curr:
            print((str(curr.data) + '->'), end=' ')
            if curr.next == self.head:
                break
            curr = curr.next
        print('none\n')


if __name__ == "__main__":
    c = CircularLinkedList()
    c.insert_at_head(10)
    c.insert_at_head(20)
    c.insert_at_end(30)
    c.insert_at_pos(2, 7)
    c.delete_by_pos(11)
    c.delete_by_val(10)
    c.print_ll()