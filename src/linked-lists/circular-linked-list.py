class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def to_list(head):
    ls = []
    if head is None:  # list empty
        return ls
    # we now know head is not none
    ls.append(head.data)
    curr = head.next
    while curr is not head:  # continue till list wraps around
        ls.append(curr.data)
        curr = curr.next
    return ls


def insert_begin_linear(head, data):
    new = Node(data)
    # empty list, new node becomes head
    if head is None:
        new.next = new  # make it circular
        return new
    curr = head
    # for adding a new head, we'll have to travel to the last node and add the new node after it
    while curr.next is not head:  # continue till list wraps around
        curr = curr.next
    # we are at the last node, insert new node
    new.next = curr.next
    curr.next = new
    return new  # new node becomes the head


def test_insert_begin_linear():
    head = None
    head = insert_begin_linear(head, 20)
    head = insert_begin_linear(head, 10)
    assert to_list(head) == [10, 20]


test_insert_begin_linear()


def insert_begin_constant(head, data):
    # neat trick, insert new node at second place and swap data with head
    new = Node(data)
    if head is None:
        new.next = new
        return new
    else:
        new.next = head.next
        head.next = new
        head.data, new.data = new.data, head.data  # swap data
        return head


def test_insert_begin_constant():
    head = None
    head = insert_begin_constant(head, 30)
    head = insert_begin_constant(head, 20)
    head = insert_begin_constant(head, 10)
    assert to_list(head) == [10, 20, 30]


test_insert_begin_constant()


def insert_end_linear(head, data):
    new = Node(data)
    if head is None:
        new.next = new
        return new
    else:
        curr = head
        while curr.next is not head:  # traverse to the last node
            curr = curr.next
        # add the new node after the last
        curr.next = new
        new.next = head  # new.next points to head now
        return head


def test_insert_end_linear():
    head = None
    head = insert_end_linear(head, 10)
    head = insert_end_linear(head, 20)
    head = insert_end_linear(head, 30)
    assert to_list(head) == [10, 20, 30]


test_insert_end_linear()


def insert_end_constant(head, data):
    # neat trick, insert new node at second place, swap data with head and new node becomes head
    new = Node(data)
    if head is None:
        new.next = new
        return new
    else:
        new.next = head.next  # insert it in second position
        head.next = new
        head.data, new.data = new.data, head.data  # swap data
        return new  # new becomes head


def test_insert_end_constant():
    head = None
    head = insert_end_constant(head, 10)
    head = insert_end_constant(head, 20)
    head = insert_end_constant(head, 30)
    assert to_list(head) == [10, 20, 30]


test_insert_end_constant()


def delete_head_linear(head):
    if head is None or head.next is None:  # empty or one node list
        return None
    else:
        curr = head
        while curr.next is not head:  # traverse to the last node
            curr = curr.next
        curr.next = head.next  # point the last node to next node of head
        return curr.next  # node after the head becomes the new head


def test_delete_head_linear():
    head = None
    head = insert_begin_constant(head, 30)
    head = insert_begin_constant(head, 20)
    head = insert_begin_constant(head, 10)
    head = delete_head_linear(head)
    assert to_list(head) == [20, 30]


test_delete_head_linear()


def delete_head_constant(head):
    # neat trick - make head effectively the second node by copying data and then unlink second node
    if head is None or head.next is None:  # empty or one node list
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next
        return head


def test_delete_head_constant():
    head = None
    head = insert_begin_constant(head, 30)
    head = insert_begin_constant(head, 20)
    head = insert_begin_constant(head, 10)
    head = delete_head_constant(head)
    assert to_list(head) == [20, 30]


test_delete_head_constant()


def delete_pos(head, pos):
    # pos starts from 1 i.e. first node is in 1st position
    if head is None:  # empty list
        return None
    elif pos == 1:
        return delete_head_constant(head)  # remove the head
    else:
        curr = head
        # for pos 2, we need to link 1st node to 3rd, so loop runs 0 times
        # for pos 3, we need to link 2nd node to 4th, so loop has to run 2 times
        # in general it's (pos - 2)
        for _ in range(pos - 2):
            curr = curr.next
        curr.next = curr.next.next  # unlink the node in question
        return head


def test_delete_pos():
    head = None
    head = insert_end_constant(head, 10)
    head = insert_end_constant(head, 20)
    head = insert_end_constant(head, 30)
    head = insert_end_constant(head, 40)
    head = insert_end_constant(head, 50)

    assert to_list(head) == [10, 20, 30, 40, 50]
    head = delete_pos(head, 1)
    assert to_list(head) == [20, 30, 40, 50]
    head = delete_pos(head, 2)
    assert to_list(head) == [20, 40, 50]
    head = delete_pos(head, 3)
    assert to_list(head) == [20, 40]


test_delete_pos()
