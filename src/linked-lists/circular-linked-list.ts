import assert from 'node:assert/strict';

type Node = {
	data: number;
	next: NodeRef;
}

type NodeRef = Node | null;

/* in circular list, the last node next points to head.
For one node list, the node points to itself
*/

function toArray(head: NodeRef): number[] {
	const arr: number[] = [];
	if (!head) {
		return arr;
	}

	let curr = head;

	// note we are using a do loop so that it executes for head.
	// otherwise the condition "curr !== head" will make while loop exit right away
	do {
		arr.push(curr.data);
		curr = curr.next!;
	} while (curr !== head)

	return arr;
}

function insertBeginLinear(head: NodeRef, data: number): Node {
	const newNode: NodeRef = { data, next: null };
	if (!head) { // list empty, the new node becomes head
		newNode.next = newNode; // this is the fist and last node. Make it circular by pointing to itself.
		return newNode;
	}

	let curr = head;
	while (curr.next !== head) { // else reach to last node as it points to head as next
		curr = curr.next!;
	}

	curr.next = newNode; // add new node after last node
	newNode.next = head; // set next of new node to head

	return newNode; // and new node becomes the new head
}

function testInsertBeginLinear() {
	let head: NodeRef = insertBeginLinear(null, 2);
	head = insertBeginLinear(head, 1);
	assert.deepEqual(toArray(head), [1, 2]);
}

testInsertBeginLinear();

function insertBeginConstant(head: NodeRef, data: number): NodeRef {
	const newNode: NodeRef = { data, next: null };
	if (!head) { // list empty, new node becomes head
		newNode.next = newNode;
		return newNode;
	}

	// now a neat trick - add new node as second node and swap data with head
	newNode.next = head.next;
	head.next = newNode;
	[head.data, newNode.data] = [newNode.data, head.data];
	return head;
}

function testInsertBeginConstant() {
	let head: NodeRef = insertBeginConstant(null, 2);
	head = insertBeginConstant(head, 1);
	assert.deepEqual(toArray(head), [1, 2]);
}

testInsertBeginConstant();

function insertEndLinear(head: NodeRef, data: number): NodeRef {
	const newNode: NodeRef = { data, next: null };
	if (!head) { // empty list, new node becomes head
		newNode.next = newNode;
		return newNode;
	}

	let curr: NodeRef = head;
	while (curr.next !== head) { // reach to last node that points to head as its next node
		curr = curr.next!;
	}

	curr.next = newNode;
	newNode.next = head;
	return head;
}

function testInsertEndLinear() {
	let head: NodeRef = insertEndLinear(null, 1);
	head = insertEndLinear(head, 2);
	assert.deepEqual(toArray(head), [1, 2]);
}

testInsertEndLinear();

function insertEndConstant(head: NodeRef, data: number): NodeRef {
	const newNode: NodeRef = { data, next: null };
	if (!head) { // empty list, new node becomes head
		newNode.next = newNode;
		return newNode;
	}

	// else insert the new node as second node and swap data with head
	newNode.next = head.next;
	head.next = newNode;
	[head.data, newNode.data] = [newNode.data, head.data];

	// new node has data of head and it becomes head
	return newNode;
}

function testInsertEndConstant() {
	let head: NodeRef = insertEndConstant(null, 1);
	head = insertEndConstant(head, 2);
	head = insertEndConstant(head, 3);
	assert.deepEqual(toArray(head), [1, 2, 3]);
}

testInsertEndConstant();

function deleteHeadLinear(head: NodeRef): NodeRef {
	if (!head || head.next === head) { // empty or one node list, deleting means retuning null
		return null;
	}

	let curr: NodeRef = head;
	while (curr.next !== head) { // reach to the last node that points to head as its next node
		curr = curr.next!;
	}

	curr.next = head.next;
	return curr.next; // second node becomes the new head
}

function testDeleteHeadLinear() {
	let head: NodeRef = insertBeginConstant(null, 3);
	head = insertBeginConstant(head, 2);
	head = insertBeginConstant(head, 1);

	head = deleteHeadLinear(head);
	assert.deepEqual(toArray(head), [2, 3]);
}

testDeleteHeadLinear();

function deleteHeadConstant(head: NodeRef): NodeRef {
	if (!head || !head.next) { // empty or one node list, deleting means retuning null
		return null;
	}

	// neat trick: make head equivalent to second node by:
	// copying second node data to head and pointing head to next of next node effectively unlinking original second node
	head.data = head.next.data;
	head.next = head.next.next;
	return head;
}

function testDeleteHeadConstant() {
	let head: NodeRef = insertEndConstant(null, 1);
	head = insertEndConstant(head, 2);
	head = insertEndConstant(head, 3);

	deleteHeadConstant(head);
	assert.deepEqual(toArray(head), [2, 3]);
}

testDeleteHeadConstant();

function deletePos(head: NodeRef, pos: number): NodeRef {
	// pos starts from 1 i.e.first node is in 1st position
	if (!head) { // empty list
		return head;
	}

	if (pos === 1) { // we need to delete head
		return deleteHeadConstant(head);
	}

	let curr: NodeRef = head;
	// for pos 2, we need to link 1st node to 3rd, so loop runs 0 times
	// for pos 3, we need to link 2nd node to 4th, so loop has to run 2 times
	// in general it's (pos - 2)
	for (let i = 0; i < pos - 2; i++) {
		curr = curr.next!;
	}

	// at this point, curr points to a node before the position to be deleted
	curr.next = curr.next!.next;

	return head;
}

function testDeletePos() {
	let head: NodeRef = insertEndConstant(null, 1);
	head = insertEndConstant(head, 2);
	head = insertEndConstant(head, 3);
	head = insertEndConstant(head, 4);

	head = deletePos(head, 1); // delete head
	assert.deepEqual(toArray(head), [2, 3, 4]);

	head = deletePos(head, 2);
	assert.deepEqual(toArray(head), [2, 4]);
}

testDeletePos();
