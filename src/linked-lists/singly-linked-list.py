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
