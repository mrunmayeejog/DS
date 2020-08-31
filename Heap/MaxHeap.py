"""
A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:
Though is computed in an array.

Heap data structure is a complete binary tree that satisfies the heap property. It is also called as a binary heap.
Max Heap - key of each node is always greater than its child node/s and the key of the root node is the largest among all other nodes
Min Heap - key of each node is always smaller than the child node/s and the key of the root node is the smallest among all other nodes.
We call heapify recursively until we get the desired value at root node. The traversal method use to achieve Array representation is Level Order

If the index of any element in the array is i, the element in the index 2i+1 will become the left child and
element in 2i+2 index will become the right child. Also, the parent of any element at index i is given by the lower bound of (i-1)/2.

In max heap:
We insert a new value at the last node and call heapify again.
We delete a given node by swapping with the last element and call heapify again.

"""
Max = 10
class Heap:
    def __init__(self):
        self.arr = [None] * Max
        self.size = 0
        self.root = None

    def return_parent_id(self, i):
        pid = (i - 1) / 2
        if int(pid) >= 0:
            return int(pid)
        return None

    def check_parent(self, i):
        pid = (i - 1) / 2
        if i > 0 and int(pid) >= 0:
            return True
        return False

    def check_right(self, i):
        rid = int((2*i) + 2)
        if rid < self.size:
            return rid

    def check_left(self, i):
        lid = int((2*i) + 1)
        if lid < self.size:
            return lid

    def heapify_up(self, index):
        """
        Check if parent exists, if yes compare values and swap
        :param index:
        :return:
        """
        while self.check_parent(index):
            pid = self.return_parent_id(index)
            # print("index " + str(index) + " pid " + str(pid))
            if self.arr[index] > self.arr[pid]:
                self.arr[index], self.arr[pid] = self.arr[pid], self.arr[index]
            index = pid

        self.root = self.arr[0]

    def insert(self, val):
        """
        Insert at last position and compare/adjust upwards ie Heapify up.
        :param val:
        :return:
        """
        if self.size == 0:
            self.arr[self.size] = val
            self.size += 1
            self.root = self.arr[0]
            return True
        else:
            self.arr[self.size] = val
            self.size += 1
            self.heapify_up(self.size - 1)

    def heapify_down(self):
        index = 0
        while self.check_left(index):
            second_max = self.check_left(index)
            if self.check_right(index):
                rid = self.check_right(index)
                if self.arr[rid] > self.arr[second_max]:
                    second_max = self.check_right(index)
            if self.arr[index] < self.arr[second_max]:
                self.arr[second_max], self.arr[index] = self.arr[index], self.arr[second_max]
            else:
                break
            index = second_max
        self.root = self.arr[0]

    def deleteNode(self):
        """
        Swap root and last node. Heapify downwards from root that is compare and adjust root to leaf.
        :param val:
        :return:
        """
        if not self.root:
            print("Heap is empty")
            return

        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], None
        self.size -= 1
        self.heapify_down()

    def print_heap(self):
        for i in range(0, self.size):
            if self.arr[i]:
                print(self.arr[i], end=" ")
        print("\n")

    def heapSort(self):
        for i in range(0, self.size - 1):
            self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
            self.size -= 1
            self.heapify_down()

        for i in range(0, Max):
            if not self.arr[i]:
                break
            print(self.arr[i], end=" ")
        print("\n")

    def peek(self):
        return self.root


if __name__ == "__main__":
    h = Heap()
    h.insert(3)
    h.insert(4)
    h.insert(7)
    h.insert(1)
    h.insert(8)
    h.insert(5)
    # h.deleteNode()
    # h.print_heap()
    h.deleteNode()
    h.print_heap()
    h.insert(12)
    h.print_heap()
    # h.heapSort()
    print(h.peek())
