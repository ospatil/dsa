import unittest


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev, self.next = None, None


def to_list(head):
    ls = []
    curr = head
    while curr is not None:
        ls.append(curr.data)
        curr = curr.next
    return ls


def insert_begin(head, data):
    new = Node(data)
    if head is not None:
        # # if there is an existing head, it becomes second node and therefore prev needs to be set
        head.prev = new
    new.next = head
    return new


def insert_end(head, data):
    new = Node(data)
    if head is None:
        return new
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        # at this point curr points to last node, add new node
        curr.next = new
        new.prev = curr
        return head


def delete_head(head):
    if head is None or head.next is None:  # empty or 1 node list
        return None
    else:
        head = head.next  # make second node as head
        head.prev = None
        return head


def delete_last(head):
    if head is None or head.next is None:  # empty or 1 node list
        return None
    else:
        curr = head
        while curr.next.next is not None:  # traverse upto second last node
            curr = curr.next
        curr.next = None  # make second last node as last node
        return head


def reverse(head):
    if head is None or head.next is None:
        return head  # for empty list return None and for list of 1 node, return head
    else:
        curr, prev = head, None
        while curr is not None:
            # store prev because when we come out of the loop, curr will be null and prev would be the last node i.e. new head
            prev = curr
            # in reversing a DLL node, the prev node becomes new next and vice versa. We do that by swapping prev and next.
            curr.prev, curr.next = curr.next, curr.prev
            # since we swapped prev and next, curr.prev points to the node that was the next node before.
            # therefore we do curr = curr.prev which is equivalent to curr = curr.next in SLL.
            curr = curr.prev
        # at the end of above loop, curr will point to None
        # therefore we maintain prev, that will point to last node that
        # now becomes the new head of the reversed list
        return prev


class DoublyLinkedListTests(unittest.TestCase):
    def test_insert_begin(self):
        head = insert_begin(None, 2)
        head = insert_begin(head, 1)
        self.assertListEqual(to_list(head), [1, 2])

    def test_insert_end(self):
        head = insert_end(None, 1)
        head = insert_end(head, 2)
        head = insert_end(head, 3)
        self.assertListEqual(to_list(head), [1, 2, 3])

    def test_delete_head(self):
        head = insert_end(None, 1)
        head = insert_end(head, 2)
        head = delete_head(head)
        self.assertListEqual(to_list(head), [2])

        head = delete_head(head)
        self.assertIsNone(head)

    def test_delete_last(self):
        head = insert_end(None, 1)
        head = insert_end(head, 2)
        head = insert_end(head, 3)

        head = delete_last(head)
        self.assertListEqual(to_list(head), [1, 2])

        head = delete_last(head)
        self.assertListEqual(to_list(head), [1])

        head = delete_last(head)
        self.assertIsNone(head)

    def test_reverse(self):
        head = None
        head = reverse(head)
        self.assertIsNone(head)

        head = insert_end(head, 1)
        head = reverse(head)
        self.assertListEqual(to_list(head), [1])

        head = insert_end(head, 2)
        head = insert_end(head, 3)
        head = reverse(head)
        self.assertListEqual(to_list(head), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
