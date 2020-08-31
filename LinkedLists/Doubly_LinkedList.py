"""
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
In simple words, a linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.
like singular LL doubly LL has two pointers next and prev.
Doubly Linkedlist APIs include
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

class dll_node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val):
        newnode = dll_node(val)
        if not self.head:
            self.head = newnode
            self.tail = self.head
            return
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        print("head at " + str(self.head.data))

    def insert_node(self, val):
        newnode = dll_node(val)
        if not self.head:
            self.head = newnode
            self.tail = newnode
            return
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def insert_at_pos(self, pos, val):
        if pos == 0:
            self.insert_at_head(val)
        else:
            newnode = dll_node(val)
            curr = self.head
            i = 1
            while curr.next:
                if pos == i:
                    nextn = curr.next
                    curr.next = newnode
                    newnode.prev = curr
                    newnode.next = nextn
                    if nextn:
                        nextn.prev = newnode
                    return
                curr = curr.next
                i += 1
            print("Invalid Position")
            return


    def delete_by_pos(self, pos):
        if not self.head:
            print("Can not delete, list is empty")
            return
        if pos == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            curr = self.head
            i = 1
            while curr.next:
                if pos == i:
                    deln = curr.next
                    if deln.next:
                        curr.next = deln.next
                        deln.next.prev = curr
                    else:
                        self.tail = curr
                        curr.next = None
                    return
                curr = curr.next
                i += 1
            self.tail = curr
            print("Invalid Position")


    def delete_by_val(self, val):
        if not self.head:
            print("Can not delete, list is empty")
            return
        if self.head.data == val:
            self.head = self.head.next
            self.head.prev = None
            return
        else:
            prev = self.head
            curr = self.head.next
            while curr:
                if curr.data == val:
                    prev.next = curr.next
                    if curr.next:
                        curr.next.prev = prev
                    else:
                        self.tail = curr.prev
                prev = curr
                curr = curr.next

    def print_node(self, node):
        if node:
            self.print_node(node.next)
            print(str(node.data) + " - > " , end="")

    def print_reverse(self):
        if not self.head:
            print("Can not delete, list is empty")
            return
        print("DLL in reverse is :")
        curr = self.head
        self.print_node(curr)
        print("none")

    def reverse_list(self):
        temp = None
        curr = self.head
        x_t = curr
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            x_h = curr
            curr = curr.prev

        self.head = x_h
        self.tail = x_t


    def print_dll(self):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        print("\nList contains : ")
        while curr:
            print(str(curr.data) + " - > " , end="")
            curr = curr.next
        print("none")


if __name__ == "__main__":
    d = DLL()
    d.insert_at_head(10)
    d.insert_node(12)
    d.insert_at_head(1)
    d.insert_at_pos(0, -1)
    d.insert_at_pos(2,3)
    d.insert_at_pos(1, 0)
    d.insert_at_pos(5, 20)
    d.delete_by_pos(5)
    d.delete_by_val(10)
    d.print_dll()
    # d.print_reverse()
    d.reverse_list()
    d.print_dll()








