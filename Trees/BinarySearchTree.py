"""
Binary search Tree is type of tree in which each node has only two children - left & right.
In BST, the left_data < root_data < right_data
Traversal is a process to visit all the nodes of a tree and may print their values too.
Because, all nodes are connected via edges (links) we always start from the root (head) node.
That is, we cannot randomly access a node in a tree. There are three ways which we use to traverse a tree −
1. In-order Traversal - Left Root Right
2. Pre-order Traversal - Root Left Right
3 .Post-order Traversal - Left Right Root

#Breadth First Traversal (Or Level Order Traversal)
#Depth First Traversals
- Inorder Traversal (Left-Root-Right)
- Preorder Traversal (Root-Left-Right)
- Postorder Traversal (Left-Right-Root)

All four traversals require O(n) time as they visit every node exactly once.
"""

from DS.Queues.Queue_using_array import *
from DS.Queues.Queues_using_LL import *

class bst_node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, val, p_node=None):
        if not self.root:
            self.root = bst_node(val)
            print("Root is " + str(self.root.data))
            return

        if not p_node:
            p_node = self.root
        curr = p_node
        if val < curr.data:
            if not curr.left:
                curr.left = bst_node(val)
                return
            else:
                self.insert_node(val, curr.left)

        if val > curr.data:
            if not curr.right:
                curr.right = bst_node(val)
                return
            else:
                self.insert_node(val, curr.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def print_inorder(self):
        if not self.root:
            print("Tree is empty")
            return
        print("\nInorder tree:")
        self.inorder(self.root)
        print("\n")

    def preorder(self, node):
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def print_preorder(self):
        if not self.root:
            print("Tree is empty")
            return
        print("\nPreorder tree:")
        self.preorder(self.root)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def print_postorder(self):
        if not self.root:
            print("Tree is empty")
            return
        print("\nPostorder tree:")
        self.postorder(self.root)

    def search_node(self, val, p_node = None):
        if not self.root:
            print("Tree is empty")
            return
        if val == self.root.data:
            print("Value found at root")
            return True
        if not p_node:
            p_node = self.root
        if val < p_node.data:
            if not p_node.left:
                print("Node not found")
            else:
                x = self.search_node(val, p_node.left)
                return x
        elif val > p_node.data:
            if not p_node.right:
                print("Node not found")
                return
            else:
                x = self.search_node(val, p_node.right)
                return x
        else:
            print("Node found")
            return True


    def bfs_traversal_queue(self):
        """
        BFS uses queues to get all nodes in given level
        :return:
        """
        queue = ArrayQueue()
        if not self.root:
            print("Tree is empty")
            return
        queue.enqueue(self.root)

        while (queue.length() > 0):
            node = queue.dequeue()
            print(node.data, end=" ")
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def bfs_traversal_ll(self):
        qq = Queues_using_LL()
        if not self.root:
            print("Tree is empty")
            return
        qq.enqueue(self.root)
        while not qq.isempty():
            node = qq.dequeue()
            print(node.data, end=" ")
            if node.left:
                qq.enqueue(node.left)
            if node.right:
                qq.enqueue(node.right)

    def parse_subtree(self, node):
        if not node.left:
            if node.right:
                left_node = node
                replaced_node = node.right
                node = node.right
                return left_node.data, replaced_node, True
            return node, None, False
        else:
            prev_node = node
            temp_node, replaced_node, bool = self.parse_subtree(node.left)
            if not bool:
                prev_node.left = replaced_node
                return temp_node.data, None, None
            else:
                prev_node.left = replaced_node
                return temp_node.data, None, None

    def delete_node(self, val, prev_node=None, curr=None):
        if not self.root:
            print("tree is empty")
            return
        if not curr:
            curr = self.root
        # if not curr.left and not curr.right:
        #     print("Value no found to delete")
        #     return

        if curr.data == val:
            print("val is at root" + str(val))
            if not curr.left and not curr.right:
                if curr == prev_node.left:
                    prev_node.left = None
                if curr == prev_node.right:
                    prev_node.right = None
                return
            else:
                node_data, replaced_node, bool = self.parse_subtree(curr.right)
                if not bool:
                    curr.data = node_data
                else:
                    curr.data = node_data
                    curr.right = replaced_node

        elif val > curr.data:
            self.delete_node(val, curr, curr.right)
            return
        elif val < curr.data:
            self.delete_node(val, curr, curr.left)
            return


if __name__ == "__main__":
    b = BinarySearchTree()
    b.insert_node(10)
    b.insert_node(15)
    b.insert_node(2)
    b.insert_node(11)
    b.insert_node(16)
    b.insert_node(5)
    b.insert_node(1)
    b.insert_node(18)
    b.insert_node(17)
    print(",,,,,,,")
    x = b.search_node(16)
    print(",,,,,,," + str(x))
    # b.delete_node(15)
    b.print_inorder()
    # b.print_preorder()
    # b.print_postorder()
    # b.search_node(15)
    # b.bfs_traversal_queue()
    # b.bfs_traversal_ll()
