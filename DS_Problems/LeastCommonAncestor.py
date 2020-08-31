"""
Least Common parent/ancestor for given nodes.
Brut approach -: Use two queues and each node as you go down DFS wise and dequeue LCA as long as both values are same.
Optimized approach is use the left and right values to find parent as each node.
"""

import DS.Trees.BinarySearchTree as Bst
from DS.Trees.BinarySearchTree import *
from DS.Queues.Queues_using_LL import *


def search_node(lca, x, y, p_node=None):
    if x <= p_node.data <= y:
        return p_node.data

    if x <= p_node.data and y <= p_node.data:
        if p_node.left:
            if p_node.left.data > lca:
                lca = p_node.left.data
            r = search_node(lca, x, y, p_node.left)
            if not r:
                return lca
            return r
    else:
        if p_node.right:
            if p_node.right.data < lca:
                lca = p_node.right.data
            r = search_node(lca, x, y, p_node.right)
            if not r:
                return lca
            return r


def check_lca(n1, n2):
    lca = 0
    if n1 < n2:
        x = n1
        y = n2
    else:
        x = n2
        y = n1
    if not b.root:
        print("Tree is empty")
        return
    if x <= b.root.data <= y:
        return b.root.data

    p_node = b.root

    if x <= p_node.data and y <= p_node.data:
        if p_node.left:
            lca = p_node.left.data
            r = search_node(lca, x, y, p_node.left)
            if not r:
                return lca
            return r
    else:
        if p_node.right:
            lca = p_node.right.data
            r = search_node(lca, x, y, p_node.right)
            if not r:
                return lca
            return r


if __name__ == "__main__":
    b = BinarySearchTree()
    b.insert_node(20)
    b.insert_node(16)
    b.insert_node(18)
    b.insert_node(13)
    b.insert_node(11)
    b.insert_node(15)
    b.insert_node(21)
    b.insert_node(25)
    b.insert_node(19)
    b.print_inorder()
    print("LCA is -> " + str(check_lca(25, 21)))
