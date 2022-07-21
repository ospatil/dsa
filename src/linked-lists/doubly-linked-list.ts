import assert from 'node:assert/strict';

type Node = {
	data: number;
	next: NodeRef;
	prev: NodeRef
};

type NodeRef = Node | null;

function toArray(head: NodeRef) {
	let curr = head;
	const list = [];
	while (curr) {
		list.push(curr.data);
		curr = curr.next;
	}

	return list;
}

function insertBegin(head: NodeRef, data: number): NodeRef {
	const newNode: NodeRef = { data, prev: null, next: null };
	if (head) { // if there is ax existing head, it becomes second node and therefore prev needs to be set
		head.prev = newNode;
	}

	newNode.next = head;
	return newNode;
}

function testInsertBegin() {
	let head: NodeRef = null;
	head = insertBegin(head, 2);
	head = insertBegin(head, 1);
	assert.deepEqual(toArray(head), [1, 2]);
}

testInsertBegin();

function insertEnd(head: NodeRef, data: number): NodeRef {
	const newNode: NodeRef = { data, next: null, prev: null };
	if (!head) { // the list is empty, newNode becomes head
		return newNode;
	}

	let curr = head;
	while (curr.next) {
		curr = curr.next;
	}

	// at this point curr points to last node
	curr.next = newNode;
	newNode.prev = curr;

	return head;
}

function testInsertEnd() {
	let head: NodeRef = null;
	head = insertEnd(head, 10);
	head = insertEnd(head, 20);
	assert.deepEqual(toArray(head), [10, 20]);
}

testInsertEnd();

function deleteFirst(head: NodeRef): NodeRef {
	return head ? head.next : head;
}

function testDeleteFirst() {
	let head: NodeRef = { data: 1, next: null, prev: null };
	head = deleteFirst(head);
	assert.equal(head, null);
	head = deleteFirst(head);
	assert.equal(head, null);
}

testDeleteFirst();

function deleteLast(head: NodeRef): NodeRef {
	// handle empty list or list with one node
	if (!head || !head.next) {
		return null;
	}

	let curr = head;
	while (curr.next?.next) { // travel upto the second-last node
		curr = curr.next;
	}

	curr.next = null;
	return head;
}

function testDeleteLast() {
	let head: NodeRef = null;
	head = insertEnd(head, 1);
	head = insertEnd(head, 2);

	head = deleteLast(head);
	assert.deepEqual(toArray(head), [1]);

	head = deleteLast(head);
	assert.deepEqual(toArray(head), []);
}

testDeleteLast();

function reverse(head: NodeRef): NodeRef {
	if (!head || !head.next) { // for empty list return null and for list of 1 node, return head
		return head;
	}

	let curr: NodeRef = head;
	let prev: NodeRef = null;
	while (curr) {
		// store prev because when we come out of the loop, curr will be null and prev would be the last node i.e. new head
		prev = curr;
		// in reversing a DLL node, the prev node becomes new next and vice versa. We do that by swapping prev and next.
		[curr.prev, curr.next] = [curr.next, curr.prev];
		// since we swapped prev and next, curr.prev points to the node that was earlier next.
		// therefore we do curr = curr.prev which is equivalent to curr = curr.next in SLL.
		curr = curr.prev;
	}

	return prev;
}

function testReverse() {
	let head: NodeRef = null;
	head = insertEnd(head, 10);
	head = insertEnd(head, 20);
	head = insertEnd(head, 30);

	head = reverse(head);

	assert.deepEqual(toArray(head), [30, 20, 10]);
}

testReverse();
