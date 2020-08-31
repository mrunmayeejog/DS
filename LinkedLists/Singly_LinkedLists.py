"""
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
In simple words, a linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.
Linkedlist APIs include
- insert_node()
- insert_at_head()
- insert_at_pos()
- search_node_by_value()
- delete_at_head()
- delete_by_value()
- delete_by_pos()
- print_list()
- print_reverse_list()
- reverse_list()
"""


class sll_node:

    def __init__(self, value):
        self.data = value
        self.next = None


class singly_linked_list:

    def __init__(self):
        self.head = None

    def print_sll(self):
        if not self.head:
            print('List is empty')
        else:
            curr = self.head
            print('\nList contains:', end=' ')
            while curr:
                print(('  ' + str(curr.data)), end=' ')
                curr = curr.next

        print('\n')

    def insert_at_head(self, value):
        newnode = sll_node(value)
        newnode.next = self.head
        self.head = newnode

    def insert_node(self, value):
        newnode = sll_node(value)
        if not self.head:
            self.head = newnode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = newnode

    def insert_node_at_pos(self, value, pos):
        newnode = sll_node(value)
        if pos == 0:
            newnode.next = self.head
            self.head = newnode
        else:
            curr = self.head
            i = 1
            while i < pos:
                if curr:
                    curr = curr.next
                    i += 1
                else:
                    print("Invalid position ")
                    return

            newnode.next = curr.next
            curr.next = newnode
            print('New value ' + str(value) + ' inserted at position ' + str(pos))

    def search_node_by_value(self, value):
        if not self.head:
            print('List is empty')
            return None
        else:
            i = -1
            curr = self.head
            while curr:
                i += 1
                print(curr.data)
                if curr.data == value:
                    print("Value found at position " + str(i))
                    return
                curr = curr.next
            print("\n Value not found")

    def delete_at_head(self):
        if not self.head:
            print('List is empty')
            return None
        self.head = self.head.next

    def delete_node_by_value(self, value):
        if not self.head:
            print('List is empty')
            return
        prev = None
        curr = self.head
        if curr.data == value:
            self.head = curr.next
            return
        else:
            while curr.next:
                prev = curr
                curr = curr.next
                if curr.data == value:
                    prev.next = curr.next
                    break
        print("Invalid value")

    def delete_by_pos(self, pos):
        if pos == 0:
            value = self.head.data
            self.head = self.head.next
            print(self.head)
            print('Value ' + str(value) + ' at pos ' + str(pos) + ' deleted')
        else:
            curr = self.head.next
            i = 1
            prev = self.head
            while curr:
                if i == pos:
                    value = curr.data
                    prev.next = curr.next
                    print('Value ' + str(value) + ' at pos ' + str(i) + ' deleted')
                    return None
                prev = curr
                curr = curr.next
                i += 1

            print('invalid pos ' + str(pos))

    def reverse_list(self):
        if not self.head:
            print('List is empty')
            return None
        else:
            prev, nextn = (None, None)
            curr = self.head
            while curr:
                    nextn = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextn
            self.head = prev

    def print_node_data(self, curr):
        if curr:
            self.print_node_data(curr.next)
            print((' >>' + str(curr.data)), end='')

    def print_reverse(self):
        if not self.head:
            print('List is empty')
            return None
        self.print_node_data(self.head)


if __name__ == '__main__':
    sll = singly_linked_list()
    sll.insert_node(10)
    sll.insert_node(20)
    sll.insert_node(30)
    sll.print_sll()
    # sll.insert_at_head(50)
    # sll.print_sll()
    # sll.insert_node_at_pos(80, 4)
    # sll.print_sll()
    # # sll.search_node_by_value(301)
    # sll.delete_by_pos(1)
    # sll.print_sll()
    # sll.delete_at_head()
    # sll.print_sll()
    # sll.delete_node_by_value(60)
    # sll.print_sll()
    sll.reverse_list()
    sll.print_sll()
