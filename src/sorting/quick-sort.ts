import assert from 'node:assert/strict';

/* quicksort
- Divide and conquer algorithm - divide a array into two parts using a pivot and sort them independently
	In merge sort the partition is simple and merge is complex,
	in quick sort, partition is complex and merge is simple.
- Worst case time: O(n²)
- Despite quadratic worst case, it's considered faster because of following reasons:
	- In-place (no aux space to partition, but the recursion call stack is still needed)
	- Cache friendly
	- Average case is O(n * logn)
	- Tail recursive (not by default in JS, we'll have to write it in that fashion)
	- Partition by function (Naive - stable, Lomuto - not stable, Hoare - not stable)
- Many languages use quicksort for non-stable scenario. FOr example - Java uses it for sorting
primitive types, for non-primitive types - it uses Timsort

Time complexity:
Best case - If the array gets divided into equal parts, then we'll be doing Θ(n) work at each
level and there will be Θ(log n) total levels in the recursion tree. Therefore total work = Θ(n * log n)

Worst case - Will happen if array is already sorted and we picked up first element as pivot
(like Hoare scheme) or it's reverse sorted and we picked last element as pivot.
In such case the list will be divided into 2 parts - first with 1 element and other with (n-1) elements.
We'll still do the same O(n) work at each level but now the levels of recursion tree will be n.
So the total complexity will be Θ(n²).

Average case: O(n * log n)

Auxiliary space:
	Worst case: Θ(n)
	best case: Θ(log n)
	Average case: Θ(log n)
*/

/* partitioning strategies */

/* naive partition scheme
	Takes Θ(n) time but makes three passes through the array
	Also requires Θ(n) aux space
*/

function partitionNaive(a: number[], p: number) { // p is position of the pivot in array
	const n = a.length;
	// move the pivot element to last so that when we iterate through the array we don't miss any smaller elements
	[a[p], a[n - 1]] = [a[n - 1], a[p]];
	const temp = [] // temporary array to hold the partitioned elements
	for (const e of a) { // loop to move all elements smaller than or equal to pivot
		if (e <= a[n - 1]) {
			temp.push(e);
		}
	}

	for (const e of a) { // loop to move all elements greater than pivot
		if (e > a[n - 1]) {
			temp.push(e);
		}
	}

	a.splice(0, n, ...temp); // third loop to copy all elements from temp to original
}

function testPartitionNaive() {
	const a = [10, 8, 2, 5, 4];
	partitionNaive(a, 4);
	// the elements are just partitioned into two parts: less than or equal to and greater than pivot
	// they are not sorted yet and therefor the result below where the two parts are unsorted
	assert.deepEqual(a, [2, 4, 10, 8, 5]);
}

testPartitionNaive();

/* lomuto partition scheme
Takes Θ(n) time but only 1 traversal through the array and Θ(1) aux space

In the function signature below:
	a - list to partition
	l - starting index
	h - ending index
We always consider the last element as pivot. We could use any element as pivot,
in that case, swap it with the last element before starting.

implementation notes:
We maintain 3 sections in the array:
	elements smaller than or equal to pivot - pointer i points to the last such element, so (i+1)st element is greater than pivot
	elements greater than pivot
	pivot - which is the last element

	------------------------------------
	| < pivot  | >= pivot  | unprocessed |
	------------------------------------
						i 					j

	Pointer j iterates through list from start to (end-1), end element being pivot.
	The current element pointed by j can have one of the two following cases:
		>= pivot: We don't have to do anything. The element is in right place. Increment j
		< pivot: Swap the element with (i+1)th element and move i forward. (i+1)th element is the first
						 element that is greater than equal to pivot. Swapping will expand the first section.

The function returns the index of final position of pivot
*/

function partitionLomuto(a: number[], l: number, h: number) {
	const pivot = a[h];
	let i = l - 1; // start with i = (low - 1) so that j can iterate from low i.e. the first element of the array
	for (let j = l; j < h; j++) { // iterate from l to (end - 1). End element is pivot
		if (a[j] < pivot) {
			i++; // increment i. (i+1) will be the position where there is first element >= pivot
			[a[j], a[i]] = [a[i], a[j]]; // swap
		}
	}

	// at this point, pivot(a[h]) needs to be put in it's right place i.e (i+1)st place.
	[a[i + 1], a[h]] = [a[h], a[i + 1]];
	return (i + 1); // return index of the final position of pivot
}

/* quicksort using Lomuto partition */
function quickSortLomuto(a: number[], l: number, h: number) {
	if (l < h) { // make sure there are at least 2 elements in the array to start with
		const p = partitionLomuto(a, l, h); // get the pivot position
		quickSortLomuto(a, l, p - 1); // recursively sort the left part before pivot
		quickSortLomuto(a, p + 1, h); // recursively sort the left part after pivot
	}
}

function testQuickSortLomuto() {
	const a = [8, 4, 7, 9, 3, 10, 5];
	quickSortLomuto(a, 0, a.length - 1)
	assert.deepEqual(a, [3, 4, 5, 7, 8, 9, 10]);
}

testQuickSortLomuto();


/* hoare's partition scheme
Takes Θ(n) time but only 1 traversal through list and Θ(1) aux space. Constants lower than Lomuto scheme, therefore faster.

Implementation notes:
	Consider first element as pivot.
	The difference with Lomuto scheme is that after sort is done, the position of pivot is not guaranteed.
	We maintain two pointers: i and j. i starts at (l-1) position i.e -1 and j starts at (h+1) i.e. one slot beyond the last in the list.
	We keep moving i to right till elements are smaller than pivot. We stop at the first element that is greater than or equal to pivot.
	We keep moving j to left till elements are greater than pivot. We stop at the first element that is less than or equal to pivot.
	We swap the elements and carry on.
	We stop the iteration when i becomes >= j. That means there are no elements in wrong position.
*/

function partitionHoare(a: number[], l: number, h: number) {
	const pivot = a[l];
	let [i, j] = [l - 1, h + 1];
	while (true) { // eslint-disable-line no-constant-condition
		do {
			i++; // move i to right
		} while (a[i] < pivot); // keep moving to right till we find out-of-place element

		do {
			j--; // move j to left
		} while (a[j] > pivot); // keep moving to left till we find out-of-place element

		// at this point, we have found violations on both sides
		if (i >= j) { // check if i and j crossed-over indicating no out-of-place elements
			// j is the position before which all elements <= pivot and after >= pivot
			return j;
		}

		[a[i], a[j]] = [a[j], a[i]]; // swap out - of - order elements
	}
}

/* quicksort using Hoare partition */
function quickSortHoare(a: number[], l: number, h: number) {
	if (l < h) { // make sure there are at least 2 elements in the array to start with
		const p = partitionHoare(a, l, h); // this is the index that separates two parts in the array
		// the following is the only difference between Lomuto and Hoare schemes
		// in Lomuto, pivot has fixed position and returns the index of it, so we'll have to limit the sort to p-1
		// in Hoare, the returned index forms the boundary and therefore we have to go upto p
		quickSortHoare(a, l, p); // recursively sort the left part before pivot
		quickSortHoare(a, p + 1, h); // recursively sort the left part after pivot
	}
}

function testQuickSortHoare() {
	const a = [8, 4, 7, 9, 3, 10, 5];
	quickSortHoare(a, 0, a.length - 1)
	assert.deepEqual(a, [3, 4, 5, 7, 8, 9, 10]);
}

testQuickSortHoare();
