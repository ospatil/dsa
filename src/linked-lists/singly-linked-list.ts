import assert from 'node:assert/strict';

type Node = {
	data: number;
	next: NodeRef;
};

type NodeRef = Node | null;

function toArray(head: NodeRef) {
	const arr = [];
	let curr = head;
	while (curr) {
		arr.push(curr.data);
		curr = curr.next;
	}

	return arr;
}

function testToArray() {
	const head: Node = { data: 1, next: { data: 2, next: { data: 3, next: null } } };
	assert.deepEqual(toArray(head), [1, 2, 3]);
}

testToArray();

function insertBegin(head: NodeRef, data: number): Node {
	return { data, next: head };
}

function testInsertBegin() {
	let head: NodeRef = null;
	head = insertBegin(head, 10);
	head = insertBegin(head, 20);
	head = insertBegin(head, 30);
	assert.deepEqual(toArray(head), [30, 20, 10]);
}

testInsertBegin();

function insertEnd(head: NodeRef, data: number): Node {
	if (!head) {
		return { data, next: null }
	}

	let curr = head;
	while (curr.next) {
		curr = curr.next;
	}

	curr.next = { data, next: null };
	return head;
}

function testInsertEnd() {
	let head: Node = { data: 10, next: { data: 20, next: { data: 30, next: null } } };
	head = insertEnd(head, 40);
	assert.deepEqual(toArray(head), [10, 20, 30, 40]);
}

testInsertEnd();

function insertPos(head: Node, pos: number, data: number): Node {
	const newNode: Node = { data, next: null };
	if (pos === 1) { // if pos is 1, new node will be the new head
		newNode.next = head;
		return newNode;
	}

	// else reach to the node before the position
	// consider the following list: 1 -> 2 -> 3 -> 4
	// when we start curr is already at position 1
	// so to add to 4th position, we need to point to 3rd and curr needs to be moved 2 times
	// for pos 3, curr needs to be moved 1 time
	// i.e. (pos - 2) times
	let curr: NodeRef = head;
	for (let i = 0; i < pos - 2; i++) {
		curr = curr.next;

		// the position passed in could be beyond the length of the list, so curr could become null
		if (!curr) {
			return head; // return original head in such case
		}
	}

	// at this point we are at desired position, add the new node after curr
	newNode.next = curr.next;
	curr.next = newNode;
	return head;
}

function testInsertPos() {
	let head: Node = { data: 2, next: { data: 3, next: { data: 5, next: { data: 6, next: null } } } };
	// insert at beginning, i.e. position 1
	head = insertPos(head, 1, 1);
	assert.deepEqual(toArray(head), [1, 2, 3, 5, 6]);
	// insert in middle
	head = insertPos(head, 4, 4);
	assert.deepEqual(toArray(head), [1, 2, 3, 4, 5, 6]);
	// insert beyond the length of list
	head = insertPos(head, 10, 10);
	assert.deepEqual(toArray(head), [1, 2, 3, 4, 5, 6]);
}

testInsertPos();

function deleteFirst(head: NodeRef): NodeRef {
	// if head is present, return next which will become new head, else return head (undefined or null)
	return head ? head.next : head;
}

function testDeleteFirst() {
	let head: NodeRef = { data: 1, next: { data: 2, next: null } };
	head = deleteFirst(head);
	assert.deepEqual(toArray(head), [2]);

	// verify
	head = deleteFirst(null as unknown as Node)!;
	assert.equal(null, head);
}

testDeleteFirst();

function deleteLast(head: NodeRef) {
	// if head is null or only one node, set head to null
	if (!head || !head.next) {
		return null;
	}

	let curr = head;
	// we need to stop at second-last node, therefore curr.next.next check
	while (curr.next?.next) {
		curr = curr.next;
	}

	curr.next = null;
	return head;
}

function testDeleteLast() {
	let head: NodeRef = { data: 1, next: { data: 2, next: { data: 3, next: null } } };
	head = deleteLast(head)!;
	assert.deepEqual(toArray(head), [1, 2]);

	head = deleteLast(head);
	assert.deepEqual(toArray(head), [1]);

	head = deleteLast(head);
	assert.equal(head, null);
}

testDeleteLast();


function search(head: NodeRef, data: unknown): number {
	let pos = 1;
	let curr = head;
	while (curr) {
		if (curr.data === data) {
			return pos;
		}

		pos++;
		curr = curr.next;
	}

	return -1;
}

function testSearch() {
	const head = { data: 10, next: { data: 4, next: { data: 24, next: null } } };
	assert.equal(search(head, 24), 3);
	assert.equal(search(head, 34), -1);
}

testSearch();

function sortedInsert(head: NodeRef, data: number): Node {
	const newNode: Node = { data, next: null };
	if (!head) { // list is empty
		return newNode;
	}

	if (data < head.data) { // since data is less than head, newNode becomes head
		newNode.next = head;
		return newNode;
	}

	// else find the node to add newNode after
	let curr = head;
	while (curr.next && curr.next.data < data) {
		curr = curr.next;
	}

	// at this point, curr points to node whose next node has data >= data, append newNode
	newNode.next = curr.next;
	curr.next = newNode;

	return head;
}

function testSortedInsert() {
	let head: NodeRef = null;
	head = sortedInsert(head, 1);
	assert.deepEqual(toArray(head), [1]);

	head = sortedInsert(head, 3);
	assert.deepEqual(toArray(head), [1, 3]);

	head = sortedInsert(head, 2);
	assert.deepEqual(toArray(head), [1, 2, 3]);
}

testSortedInsert();

function reverseUsingStack(head: NodeRef): NodeRef {
	const stack = [];
	let curr = head;
	// store the data in stack
	while (curr) {
		stack.push(curr.data);
		curr = curr.next;
	}

	curr = head;
	while (curr) {
		curr.data = stack.pop()!;
		curr = curr.next;
	}

	return head;
}

function testReverseUsingStack() {
	let head: NodeRef = { data: 1, next: { data: 2, next: { data: 3, next: null } } }
	head = reverseUsingStack(head);
	assert.deepEqual(toArray(head), [3, 2, 1]);
}

testReverseUsingStack();

function reverse(head: NodeRef): NodeRef {
	let curr = head;
	let prev = null;
	while (curr) {
		const { next } = curr;
		curr.next = prev;
		prev = curr;
		curr = next;
	}

	// at this point, curr points to the last null and
	// prev points to the last node which will be the new head
	return prev;
}

function testReverse() {
	let head: NodeRef = { data: 1, next: { data: 2, next: { data: 3, next: null } } };
	head = reverse(head);
	assert.deepEqual(toArray(head), [3, 2, 1]);
}

testReverse();

function reverseRec(curr: NodeRef, prev: NodeRef = null): NodeRef {
	// the idea is we reverse the first link and then make recursive call to reverse next link
	if (!curr) { // base case, compare to iterative reverse above. We reached to the end of list and prev points to the last node that is new head
		return prev;
	}

	const { next } = curr; // store reference to next node
	curr.next = prev; // reverse the link
	return reverseRec(next, curr); // continue the reversal with next as curr node and curr as previous for next call
}

function testReverseRec() {
	let head: NodeRef = { data: 1, next: { data: 2, next: { data: 3, next: null } } };
	head = reverseRec(head);
	assert.deepEqual(toArray(head), [3, 2, 1]);
}

testReverseRec();
