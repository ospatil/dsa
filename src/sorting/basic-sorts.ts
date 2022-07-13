import assert from 'node:assert/strict';

/* bubble sort
The idea is in each iteration we bubble the highest value to the end of the array.
	1st iteration -> 0 elements in their right position
	2nd iteration -> last element in right position
	3rd iteration -> last 2 elements in right elements

Time complexity: O(n²)

Characteristics: in-place, stable
What is stable? If there are two elements with same value, their order is maintained after sorting.
*/

function bubbleSort(a: number[]) {
	const n = a.length;
	for (let i = 0; i < n; i++) {
		let swapped = false; // if no swaps happen, the list is sorted.
		// why n - i - 1 ? because in each iteration last some elements will be in right position
		// i = 0, no elements in right place
		// i = 1, last element in right place
		// i = 2, last 2 elements on right place
		// therefore we don't need to consider last (n-i-1) elements in comparison
		for (let j = 0; j < (n - i - 1); j++) {
			if (a[j] > a[j + 1]) {
				[a[j], a[j + 1]] = [a[j + 1], a[j]];
				swapped = true;
			}
		}

		if (!swapped) {
			break;
		}
	}
}

function testBubbleSort() {
	const a = [6, 4, 8, 3, 10];
	bubbleSort(a);
	assert.deepEqual(a, [3, 4, 6, 8, 10]);
}

testBubbleSort();

/* selection Sort:
Time complexity: Θ(n²)
Does less memory writes compared to quicksort and mergesort etc. (cyclesort is optimal for memory writes)
It's the same basic idea for heap sort
Not stable
In-place

Basic idea is we find min element and put it in 0th position, we find second minimum and put it in 1st position and so on.
*/
function selectionSort(a: number[]) {
	const n = a.length;
	for (let i = 0; i < n - 1; i++) {
		let min = i; // index of min element
		// iterate on subarray from i + 1 to end to find index of min element
		// i = 0, subarray will be 1 to end
		// i = 1, subarray will be 2 to end and so on
		for (let j = i + 1; j < n; j++) {
			if (a[j] < a[min]) { // found new smaller element
				min = j;
			}
		}

		[a[i], a[min]] = [a[min], a[i]]; // move the min element to right position, i.e ith position
	}
}

function testSelectionSort() {
	const a = [6, 4, 8, 3, 10];
	selectionSort(a);
	assert.deepEqual(a, [3, 4, 6, 8, 10]);
}

testSelectionSort();

/* insertion sort
Time complexity:
	Θ(n²) worst case when array is reverse sorted,
	Θ(n) best case of already sorted array,
	So it's O(n²)
Stable
In-place
Used in practice for small array in hybrid sort algorithms like Timsort (python) and Introsort (C++)

Idea:
We maintain two parts in the array: sorted and unsorted.
We iterate on the array, put each element at right position in sorted part, grow the sorted part and continue.
In the beginning, we consider a[0] as sorted part and start iteration from a[1].
*/
function insertionSort(a: number[]) {
	for (let i = 1; i < a.length; i++) { // start iterating from 1st element
		const x = a[i];
		let j = i - 1; // at beginning, j will be the last element in th sorted part of list
		// find the right position for x in the sorted part.Move all elements that are
		// greater than x to right to make space for x at right place.
		while (j >= 0 && x < a[j]) {
			a[j + 1] = a[j];
			j--;
		}

		// at this point, j points to first smaller element than x, so the slot for x is is at(j + 1).
		a[j + 1] = x;
	}
}

function testInsertionSort() {
	const a = [6, 4, 8, 3, 10];
	insertionSort(a);
	assert.deepEqual(a, [3, 4, 6, 8, 10]);
}

testInsertionSort();
