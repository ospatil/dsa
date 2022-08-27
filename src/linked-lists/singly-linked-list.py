class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def to_list(head):
    ls = []
    curr = head
    while curr is not None:
        ls.append(curr.data)
        curr = curr.next
    return ls


def insert_begin(head, data):
    new = Node(data)
    new.next = head
    return new  # new node becomes new head


def test_insert_begin():
    head = None
    head = insert_begin(head, 20)
    head = insert_begin(head, 10)
    assert to_list(head) == [10, 20]


test_insert_begin()


def insert_end(head, data):
    new = Node(data)
    if head is None:  # empty list, new node becomes new head
        return new
    curr = head
    while curr.next is not None:  # traverse to the end
        curr = curr.next
    curr.next = new  # add new node at the end
    return head


def test_insert_end():
    head = None
    head = insert_end(head, 10)
    head = insert_end(head, 20)
    assert to_list(head) == [10, 20]


test_insert_end()


def insert_pos(head, pos, data):
    new = Node(data)
    if pos == 1:  # if pos is 1, new node will be the new head
        new.next = head
        return new
    # else reach to the node before the position
    # consider the following list: 1 -> 2 -> 3 -> 4
    # when we start curr is already at position 1
    # so to add to 4th position, we need to point to 3rd and curr needs to be moved 2 times
    # for pos 3, curr needs to be moved 1 time
    # i.e. (pos - 2) times
    curr = head
    for i in range(pos - 2):
        curr = curr.next
        # the position passed in could be beyond the length of the list, so curr could become None
        if curr is None:
            return head  # return original head in such case
    new.next = curr.next
    curr.next = new
    return head


def test_insert_pos():
    head = None
    head = insert_end(head, 2)
    head = insert_end(head, 3)
    head = insert_end(head, 5)
    head = insert_end(head, 6)

    # insert at beginning
    head = insert_pos(head, 1, 1)
    assert to_list(head) == [1, 2, 3, 5, 6]

    # insert in middle
    head = insert_pos(head, 4, 4)
    assert to_list(head) == [1, 2, 3, 4, 5, 6]

    # insert beyond the length of the list
    head = insert_pos(head, 10, 10)
    assert to_list(head) == [1, 2, 3, 4, 5, 6]


test_insert_pos()


def delete_first(head):
    if head is None:
        return None
    else:
        return head.next


def test_delete_first():
    head = Node(1)
    head.next = Node(2)

    head = delete_first(head)
    assert to_list(head) == [2]

    head = delete_first(head)
    assert head is None


test_delete_first()


def delete_last(head):
    if head is None or head.next is None:  # empty or one node list
        return None
    else:
        curr = head
        # we need to stop at second-last node, therefore curr.next.next check
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
    return head


def test_delete_last():
    head = Node(1)
    head.next = Node(2)

    head = delete_last(head)
    assert to_list(head) == [1]

    head = delete_last(head)
    assert head is None


test_delete_last()


# Return the position of data if found else return -1. Position is 1 based.
def search(head, data):
    pos, curr = 1, head
    while curr is not None:
        if curr.data == data:
            return pos
        pos += 1
        curr = curr.next
    return -1


def test_search():
    head = Node(10)
    head.next = Node(4)
    head.next.next = Node(24)

    assert search(head, 24) == 3
    assert search(head, 34) == -1


test_search()


def sorted_insert(head, data):
    new = Node(data)
    if head is None:  # if list is empty, new node becomes head
        return new
    elif data < head.data:  # new data less than head, new node becomes head
        new.next = head
        return new
    else:
        curr = head
        # find the node whose next's data is greater than new data
        while curr.next is not None and curr.next.data < data:
            curr = curr.next
        new.next = curr.next
        curr.next = new
        return head


def test_sorted_insert():
    head = sorted_insert(None, 2)
    head = sorted_insert(head, 3)
    head = sorted_insert(head, 4)
    head = sorted_insert(head, 1)
    assert to_list(head) == [1, 2, 3, 4]


test_sorted_insert()


def reverse_using_stack(head):
    stack = []
    curr = head
    while curr is not None:
        stack.append(curr.data)
        curr = curr.next
    curr = head
    while curr is not None:
        curr.data = stack.pop()
        curr = curr.next
    return head


def test_reverse_using_stack():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    head = reverse_using_stack(head)
    assert to_list(head) == [3, 2, 1]


test_reverse_using_stack()


def reverse(head):
    # three pointer technique
    curr, prev = head, None
    while curr is not None:
        next = curr.next  # store reference to next
        curr.next = prev
        prev = curr  # prev becomes curr
        curr = next  # curr becomes next
    # at this point, curr points to the last null and prev points to the last node which will be the new head
    return prev


def test_reverse():
    head = Node(10)
    head = insert_end(head, 20)
    head = insert_end(head, 30)
    head = insert_end(head, 40)

    head = reverse(head)
    assert to_list(head) == [40, 30, 20, 10]


test_reverse()


def reverse_rec(curr, prev=None):
    # the idea is we reverse the first link and then make recursive call to reverse next link
    if curr is None:
        # base case, compare to iterative reverse above. We reached to the end of list and prev points to the last node that is new head
        return prev
    next = curr.next  # store reference to next node
    curr.next = prev  # reverse the link
    # continue the reversal with next as curr node and curr as previous for next call
    return reverse_rec(next, curr)


def test_reverse_rec():
    head = Node(10)
    head = insert_end(head, 20)
    head = insert_end(head, 30)
    head = insert_end(head, 40)

    head = reverse_rec(head)
    assert to_list(head) == [40, 30, 20, 10]


test_reverse_rec()
