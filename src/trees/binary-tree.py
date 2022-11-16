"""
Consider the following binary tree:
        10
       /  \
      20  30
      / \  \
     40 50 60
       / \
      70 80

Traversals:
Breadth-first i.e Level order: 10 20 30 40 50 60 70 80

Depth-first:
Three popular ways. The order is with respect to root.

Inorder:    left root right
            40 20 70 50 80 10 30 60
Preorder:   root left right
            10 20 40 50 70 80 30 60
Postorder:  left right root
            40 70 80 50 20 60 30 10

Variations of tree and uses:
* Binary search tree:
* Binary heap: Mainly used to represent priority queues.
* B and B+ tree: Database indexes
* Spanning and shortest path trees: Used in computer networks
    Bridges use spanning tree to forward the packets
    routers use shortest path trees to to route data
* Parse tree, expression tree: in compilers
* Trie: Used to represent dictionary, supports operations like prefix search
* Suffix tree: used for fast searches in string, if you have pattern and text
    We can preprocess text, build suffix tree and search patterns in this tree
    Time is proportional to length of pattern and not of the string.
* Binary index tree: Used for range query searches. Faster for limited set of operations.
* Segment tree: Used for range query searches. More powerful.

Number of children is a tree is called degree.
Binary trees are most common type of tree.
Binary tree can have 0, 1 or 2 children.
Binary tree can also be represented as array.
"""

from collections import deque
import math
import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, ls):
    """
    Time complexity: 𝛳(n)
    Aux Space: 𝛳(h) where h is height since at any time there will be h function calls on call stack
    """
    if root is not None:
        inorder(root.left, ls)
        ls.append(root.data)
        inorder(root.right, ls)


def preorder(root, ls):
    """
    Time complexity: 𝛳(n)
    Aux Space: 𝛳(h) where h is height since at any time there will be h function calls on call stack
    """
    if root is not None:
        ls.append(root.data)
        preorder(root.left, ls)
        preorder(root.right, ls)


def postorder(root, ls):
    """
    Time complexity: 𝛳(n)
    Aux Space: 𝛳(h) where h is height since at any time there will be h function calls on call stack
    postorder is not tail-recursive, while other two are.
    """
    if root is not None:
        postorder(root.left, ls)
        postorder(root.right, ls)
        ls.append(root.data)


def size(root):
    """
    Time complexity: 𝛳(n)
    Aux Space: 𝛳(h) where h is height since at any time there will be (h+1) function calls on call stack
    """
    # no of nodes in the binary tree
    if root is None:
        return 0
    else:
        return 1 + size(root.left) + size(root.right)


def get_max(root):
    """
    Time complexity: 𝛳(n)
    Aux Space: 𝛳(h) where h is height since at any time there will be (h+1) function calls on call stack
    """
    # return -infinity for none
    if root is None:
        return -math.inf
    else:
        return max(root.data, get_max(root.left), get_max(root.right))


def search(root, data):
    """
    Time complexity: O(n)
    Aux Space: 𝛳(h) where h is height since at any time there will be (h+1) function calls on call stack
    """
    if root is None:
        return False
    elif root.data == data:
        return True
    else:
        return search(root.left, data) or search(root.right, data)


def height(root):
    """
    Time complexity: 𝛳(n)
    Aux Space: 𝛳(h) where h is height since at any time there will be (h+1) function calls on call stack

    There are two conventions for height of a tree:
    1. Maximum number of nodes on longest (root to leaf) path
        height of single node tree is 1
        height of empty tree is 0
    2. Maximum number of edges on longest path
        height of single node tree is 0
        height of empty tree is -1
    We'll use 1.
    """
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))  # +1 for the root node


def inorder_iter(root):
    """
    Time complexity: 𝛳(n)
    Aux Space: 𝛳(h) at any points there will be "height" no. of nodes in the stack
    """
    # we traverse to leftmost leaf by pushing nodes in a stack,
    # once there, we print its data. When that happens, it's left subtree will have been processed completely
    # we then continue with the right subtree and process its left subtrees
    if root is None:
        return

    roots = []
    result = []  # will hold result of the traversal
    curr = root
    while curr is not None:
        roots.append(curr)
        curr = curr.left
    # we are at the leftmost leaf, time to pop the stack
    while len(roots) > 0:
        curr = roots.pop()
        result.append(curr.data)
        curr = curr.right  # now go to the right subtree
        while curr is not None:
            roots.append(curr)
            curr = curr.left
    return result


def preorder_iter(root):
    """
    Time complexity: 𝛳(n)
    Aux Space: O(n) as we are pushing both right and left nodes in stack
    """
    if root is None:
        return
    roots = [root]
    result = []
    # consider a simple tree
    #   10
    # 20  30
    # We need to print 10, then 20 and then 30
    # we are using stack which is LIFO, therefore, in the code below,
    # we push 30 i.e right first and then 20 i.e left so that left
    # is popped first.
    while len(roots) > 0:
        curr = roots.pop()
        result.append(curr.data)
        if curr.right is not None:
            roots.append(curr.right)
        if curr.left is not None:
            roots.append(curr.left)
    return result


def levelorder(root):
    """
    Time complexity: 𝛳(n)
    Aux Space: O(n) as we are pushing a level in the queue i.e. width of the binary tree
    """
    if root is None:
        return
    # use queue to store nodes
    q = deque()
    result = []
    q.append(root)
    while len(q) > 0:
        curr = q.popleft()
        result.append(curr.data)
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
    return result


class BinaryTreeTests(unittest.TestCase):
    def create_test_tree(self):
        # tree
        #     10
        #  20    30
        #      40  50
        root = Node(10)
        root.left = Node(20)
        root.right = Node(30)
        root.right.left = Node(40)
        root.right.right = Node(50)
        return root

    def test_inorder(self):
        root = self.create_test_tree()
        ls = []
        inorder(root, ls)
        self.assertListEqual(ls, [20, 10, 40, 30, 50])

    def test_preorder(self):
        root = self.create_test_tree()
        ls = []
        preorder(root, ls)
        self.assertListEqual(ls, [10, 20, 30, 40, 50])

    def test_postorder(self):
        root = self.create_test_tree()
        ls = []
        postorder(root, ls)
        self.assertListEqual(ls, [20, 40, 50, 30, 10])

    def test_size(self):
        root = self.create_test_tree()
        self.assertEqual(size(root), 5)

    def test_get_max(self):
        root = self.create_test_tree()
        self.assertEqual(get_max(root), 50)

    def test_search(self):
        root = self.create_test_tree()
        self.assertTrue(search(root, 40))
        self.assertFalse(search(root, 60))

    def test_height(self):
        root = self.create_test_tree()
        self.assertEqual(height(root), 3)

    def test_inorder_iter(self):
        root = self.create_test_tree()
        self.assertListEqual(inorder_iter(root), [20, 10, 40, 30, 50])

    def test_preorder_iter(self):
        root = self.create_test_tree()
        self.assertListEqual(preorder_iter(root), [10, 20, 30, 40, 50])

    def test_levelorder(self):
        root = self.create_test_tree()
        self.assertListEqual(levelorder(root), [10, 20, 30, 40, 50])


if __name__ == "__main__":
    unittest.main()
