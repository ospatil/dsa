import assert from 'node:assert/strict';

/* merge two sorted lists
i/p: a = [10, 15, 20], b = [5, 6, 6, 30]
o/p: [5, 6, 6, 10, 15, 20, 30]
*/

/* mergeListsNaive
Time complexity: O((m + n) * log(m + n)) where m = len(a) and n = len(b)
This solution doesn't use the fact that both lists are sorted.
*/
function mergeListsNaive(arr1: number[], arr2: number[]): number[] {
	const res = [...arr1, ...arr2];
	res.sort((a, b) => a - b);
	return res;
}

assert.deepEqual(
	mergeListsNaive([10, 15, 20], [5, 6, 6, 30]),
	[5, 6, 6, 10, 15, 20, 30],
);

/* mergeLists
Time Complexity: Θ(m+n)
This solution makes use of the fact that both lists are sorted.
*/
function mergeLists(a: number[], b: number[]): number[] {
	const res = [];
	let [i, j] = [0, 0];
	while (i < a.length && j < b.length) {
		// run till we run out of one of the lists
		if (a[i] < b[j]) {
			// copy the smaller element to result array and increment the pointer
			res.push(a[i++]);
		} else {
			res.push(b[j++]);
		}
	}

	// at this point one of the list is exhausted, so copy the remaining elements
	// from the list still having elements into the result.
	res.push(...a.slice(i), ...b.slice(j));

	return res;
}

assert.deepEqual(
	mergeLists([10, 15, 20], [5, 6, 6, 30]),
	[5, 6, 6, 10, 15, 20, 30],
);

/* merge sub-arrays of an array
i/p: a = [10, 15, 20, 11, 13], low = 0, mid = 3, high = 4
o/p: [10, 11, 13, 15, 20]

i/p: a = [5, 8, 12, 14, 7], low = 0, mid = 3, high = 4
o/p: [5, 7, 8, 12, 14]

Note that the elements from low to mid are sorted and so are elements from mid+1 to high.
We need to merge all elements from low to high in the same array and get all elements sorted from Low <= mid < high.

Implementation idea
Copy elements from low to mid into an auxiliary array called left.
Copy the elements from mid+1 to high into the auxiliary array called right.
Merge left and right using the merge function like mergeLists above.
*/
function merge(a: number[], low: number, mid: number, high: number) {
	// (mid + 1) to include mid in the left and (high + 1) to include high in the right array
	const [left, right] = [a.slice(low, mid + 1), a.slice(mid + 1, high + 1)];
	let [i, j] = [0, 0]; // indexes for left and right arrays respectively
	let k = low; // index in the original a array where we'll start appending elements from left or right arrays.

	while (i < left.length && j < right.length) {
		if (left[i] <= right[j]) {
			// append from left and increment i and k
			a[k++] = left[i++];
		} else {
			// append from right and increment j and k
			a[k++] = right[j++];
		}
	}

	// at this point, one of the arrays is exhausted, so copy remaining elements from the other
	while (i < left.length) {
		a[k++] = left[i++];
	}

	while (j < right.length) {
		a[k++] = right[j++];
	}
}

function testMerge() {
	let a = [10, 15, 20, 11, 13];
	merge(a, 0, 2, 4);
	assert.deepEqual(a, [10, 11, 13, 15, 20]);
	a = [5, 8, 12, 14, 7];
	merge(a, 0, 3, 4);
	assert.deepEqual(a, [5, 7, 8, 12, 14]);
}

testMerge();

/* merge sort

- Divide and conquer algorithm - divide a array into two parts and sort them independently
	partition the array into two sub-arrays
	recursively sort the two sub-arrays
	merge the sorted sub-arrays

Time complexity:
	At each invocation, we split the input into 2 parts and make recursive calls.
	Therefore, there height of recurrence tree will be O(log n) and at each level the work we do
	is merging the sorted parts i.e. Θ(n) work.
	Therefore time complexity = O(n * log n)

Auxiliary space: O(n) for merge function
*/
function mergeSort(a: number[], l: number, r: number) {
	if (r > l) {
		// there should be at least 2 elements in the array for sorting
		const m = Math.floor((l + r) / 2); // calculate mid-point
		mergeSort(a, l, m); // recursively sort the left array
		mergeSort(a, m + 1, r); // recursively sort the right array
		merge(a, l, m, r); // merge two sorted arrays
	}
}

function testMergeSort() {
	const a = [10, 5, 30, 15, 7];
	mergeSort(a, 0, a.length - 1);
	assert.deepEqual(a, [5, 7, 10, 15, 30]);
}

testMergeSort();
