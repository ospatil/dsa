import unittest

"""
Binary search tree

- For every node, data on left side is smaller and data on right is greater.
- All data is distinct.

Ex:
        50
      /    \
     30    70
    / \    / \
   10 40  60 80

- Time complexity of search in BST: O(h) where h is the height of tree.
- Inorder traversal of BST always results in sorted data.
- Smallest data is always leftmost leaf and largest the rightmost leaf.

- If keys are in sorted increasing order BST turns into a linked list
    ex: 5, 10, 20, 30 (right-skewed)
  If keys are sorted in decreasing order the tree turns into left-skewed tree
    5
    \
    10
     \
     20
      \
      40

Ideally, we want balanced BST that allow all operations in O(log n) time.
Examples - AVL tree, Red-black tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, acc):
    if root is not None:
        inorder(root.left, acc)
        acc.append(root.data)
        inorder(root.right, acc)


def search(root, data):
    """
    Time complexity: O(h) where h is height of BST
    Aux space: O(h)
    """
    if root is None:
        return False
    elif root.data == data:
        return True
    elif root.data > data:  # go left
        return search(root.left, data)
    else:  # go right
        return search(root.right, data)


def searchIter(root, data):
    """
    Time complexity: O(h) where h is height of BST
    Aux space: O(1)
    """
    while root is not None:
        if root.data == data:
            return True
        elif root.data > data:
            root = root.left
        else:
            root = root.right
    return False


def insert(root, data):
    """
    Time complexity: O(h) where h is height of BST
    Aux space: O(h)
    """
    # returns root, changes root only when BST is empty, the insertion always happens at leaf level for non-empty BST
    if root is None:
        return Node(data)
    elif root.data == data:
        return root
    elif root.data > data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def insertIter(root, data):
    """
    Time complexity: O(h) where h is height of BST
    Aux space: O(1)
    """
    new = Node(data)
    parent, curr = None, root
    # traverse and find out the parent for the new data
    # curr tracks the root for each iteration. When it becomes None, we have reached the correct leaf position for insertion.
    # So, basically, we come out of the loop when curr becomes None and at that point parent points node that will be parent of
    # the new node.
    while curr is not None:
        # parent will eventually point to node to which new leaf node will be attached
        parent = curr
        if curr.data == data:
            return root  # since the data already exists, we return existing root
        elif curr.data > data:
            curr = curr.left
        else:
            curr = curr.right
    if parent is None:  # empty tree case, so create new node and return it as root
        return new
    elif parent.data > data:  # add as a left node
        parent.left = new
    else:
        parent.right = new  # add as a right node
    return root


def __find_successor(node):
    while node.left is not None:
        node = node.left
    return node


def delete(root, data):
    """
    Time complexity: O(h) where h is height of BST
    Aux space: O(h)

    While deleting, we need to maintain BST property
    Three cases to consider:
    1. Delete leaf - easiest deletion
    2. Non-leaf with only 1 child - delete the node and replace it with child
    3. Non-leaf with both children -
        To maintain BST property, we can replace the node with one of the following:
        1. Closest lower value
        2. Closest higher value.
        We'll always replace it with closest higher value.
        Closest higher value in BST is inorder successor and it's the leftmost leaf in right subtree.
        Since it's leaf we can delete it easily and replace the dat of the node we want to delete with its data.
        (On related note, closest lower value in BST is inorder predecessor)
    """
    if root is None:  # empty tree, return
        return
    if root.data > data:
        # traverse left subtree. It will return new root of left subtree.
        root.left = delete(root.left, data)
    elif root.data < data:
        # traverse right subtree. It will return new root of right subtree.
        root.right = delete(root.right, data)
    else:  # this is the case where root points to the node to be deleted
        # if left node is None, return right node that replaces root
        if root.left is None:
            return root.right
        # if right node is None, return left node that replaces root
        if root.right is None:
            return root.left
        else:  # find the inorder successor i.e. leftmost leaf in right subtree
            successor = __find_successor(root.right)
            root.data = successor.data  # replace root with data from successor
            root.right = delete(
                root.right, successor.data
            )  # delete the inorder successor node
    return root


def floor(root, val):
    """
    Find the largest value in tree that is smaller than val

    Time complexity: O(h)
    Aux space: O(1)
    """
    res = None
    while root is not None:
        if root.data == val:  # we found it, return the node
            return root
        elif root.data > val:  # root data is greater than x, continue in left subtree
            root = root.left
        else:
            # root is less than x and could be potential floor
            # assign it to res and continue traversing the right subtree
            # for closer floor
            res = root
            root = root.right
    return res


def ceil(root, val):
    """
    Find the smallest value in tree that is greater than x

    Time complexity: O(h)
    Aux space: O(1)
    """
    res = None
    while root is not None:
        if root.data == val:
            return root
        elif (
            root.data < val
        ):  # since root is smaller and we are looking for ceiling, continue with right subtree
            root = root.right
        else:
            # root is greater, it could be potential ceiling, assign it to result and continue down the left subtree
            res = root
            root = root.left
    return res


class BinarySearchTreeTests(unittest.TestCase):
    def create_test_bst(self):
        """
              10
             /  \
            5   30
           /    / \
          2    25 40
        """
        root = Node(10)
        root.left = Node(5)
        root.left.left = Node(2)
        root.right = Node(30)
        root.right.left = Node(25)
        root.right.right = Node(40)

        return root

    def test_inorder(self):
        root = self.create_test_bst()
        res = []
        inorder(root, res)
        self.assertListEqual(res, [2, 5, 10, 25, 30, 40])

    def test_search(self):
        root = self.create_test_bst()
        self.assertTrue(search(root, 30))
        self.assertFalse(search(root, 50))

    def test_searchIter(self):
        root = self.create_test_bst()
        self.assertTrue(search(root, 25))
        self.assertFalse(search(root, 50))

    def test_insert(self):
        root = insert(None, 40)
        root = insert(root, 20)
        root = insert(root, 30)
        root = insert(root, 100)
        root = insert(root, 70)
        root = insert(root, 60)
        root = insert(root, 200)
        res = []
        inorder(root, res)
        self.assertListEqual(res, [20, 30, 40, 60, 70, 100, 200])

    def test_insertIter(self):
        root = insertIter(None, 40)
        root = insertIter(root, 20)
        root = insertIter(root, 30)
        root = insertIter(root, 100)
        root = insertIter(root, 70)
        root = insertIter(root, 60)
        root = insertIter(root, 200)
        res = []
        inorder(root, res)
        self.assertListEqual(res, [20, 30, 40, 60, 70, 100, 200])

    def test_delete(self):
        """
               20
              /  \
            10     30
            / \    / \
           5  15  25 40
        """
        root = Node(20)
        root.left = Node(10)
        root.left.left = Node(5)
        root.left.right = Node(15)
        root.right = Node(30)
        root.right.left = Node(25)
        root.right.right = Node(40)

        res = []
        inorder(root, res)
        self.assertListEqual(res, [5, 10, 15, 20, 25, 30, 40])

        # delete leaf node (5)
        root = delete(root, 5)
        res = []
        inorder(root, res)
        self.assertListEqual(res, [10, 15, 20, 25, 30, 40])

        # delete intermediate node with one leaf node (10)
        root = delete(root, 10)
        res = []
        inorder(root, res)
        self.assertListEqual(res, [15, 20, 25, 30, 40])

        # delete a node with both leaf nodes (20)
        root = delete(root, 20)
        res = []
        inorder(root, res)
        self.assertListEqual(res, [15, 25, 30, 40])

    def test_floor(self):
        root = self.create_test_bst()
        self.assertEqual(floor(root, 6).data, 5)
        self.assertEqual(floor(root, 10).data, 10)
        self.assertIsNone(floor(root, 1))

    def test_ceil(self):
        root = self.create_test_bst()
        self.assertEqual(ceil(root, 10).data, 10)
        self.assertEqual(ceil(root, 26).data, 30)
        self.assertIsNone(ceil(root, 50))


if __name__ == "__main__":
    unittest.main()
