import math
import unittest

"""
Binary heap
    - used in heapsort
    - Used to implement priority queue

There are two types
1. Min heap - highest priority item is assigned lowest value
2. Max heap - highest priority item is assigned highest value

Binary heap is a complete binary tree (stored as an array).
Complete binary tree is a binary tree whose all levels are completely
filled except possibly the last level and the last level has to be filled
from left to right.

Array representation:

Left child of node at index i: left(i) = 2i + 1
right(i) = 2i + 2
parent(i) = floor((i - 1)/2)

Array representation has its usual advantages:
    1. Contiguous storage therefore random access
    2. cache friendliness
    3. Since it's a complete binary tree, the height is minimum possible height (log n)

Min Heap
    - complete binary tree
    - every node has value smaller than its descendants


Min heap implementation:
Main operations:
    - constructor (simple)
    - insert
    - extract min
    - decrease key
    - delete
    - constructor enhanced with build heap

Utility functions:
    - left child
    - right child
    - parent
    - min heapify
"""


class MinHeap:
    def __init__(self, ls=[]):
        """
        When l is provided, build heap using it.
        Naive approach: Sort the arr and then build heap
        Time complexity: O(n log n)

        Efficient approach: find the position of the last non-leaf node and perform
        the heapify operation of each non-leaf node in reverse level order.
        Last non-leaf node is going to be the parent of last-node.
        i.e. parent of node at (len(l)-1) index
        i.e. Node at index ((len(l)-1) - 1)//2.

        Time complexity: O(n)
        https://www.geeksforgeeks.org/building-heap-from-array/
        """
        self.arr = ls
        i = (len(ls) - 2) // 2
        while i >= 0:  # carry out heapifying till we reach the root
            self.heapify(i)
            i -= 1

    def parent(self, i):
        return (i - 1) // 2

    def lchild(self, i):
        return (2 * i) + 1

    def rchild(self, i):
        return (2 * i) + 2

    def heapify(self, i):
        """
        Fixes min heap whose root might be violating min heap property

        Time complexity: O(log n)
        Aux space: O(log n)
        """
        arr = self.arr
        # get the left and right children of i
        lt = self.lchild(i)
        rt = self.rchild(i)
        # we'll assume that i is smallest to begin with and will find which of three: i, left child or right child is smallest
        smallest = i
        n = len(arr)
        # < n condition makes sure we don't go beyond size of the list in the recursive calls
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt
        # if root is not smallest, swap and carry on heapifying the concerned subtree
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.heapify(smallest)

    def insert(self, x):
        """
        Time complexity: O(log n)

        The idea is to append x to the end of the array - O(1) operation
        But if it is smaller than its parents, it will violate min heap property.
        Therefore, we travel the height of the binary heap, and keep swapping x with parent (and grant-parent etc)
        as needed till it's in its intended place.
        This operation is O(log n) since traveling across the height of binary heap is log of size operation.
        """
        arr = self.arr
        arr.append(x)
        # move it in its right place
        i = len(arr) - 1  # current index of x
        # continue swap till we either reach root (i = 0) or parent is smaller or equal (arr[self.parent(i)] > arr[i])
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]  # swap with parent
            i = p  # move i to parent and continue

    def extract_min(self):
        """
        Remove min from the heap and use heapify to make sure the min heap property holds true for rest of the array

        Time complexity: O(log n)

        If we remove an element from anywhere other than last position in an array, we'll need to move all other elements
        and it will be linear operation.
        To achieve "log n" time, removing last element will be constant time. so that's what we do.
            1. swap min with last (constant)
            2. pop last (constant)
            3. then heapify (log n).
        """
        arr = self.arr
        if len(arr) == 0:  # deal with empty heap
            return math.inf
        res = arr[0]  # it's the root element of the heap i.e. the smallest element
        arr[0] = arr[-1]  # assign the last element value to the root element
        arr.pop()  # remove the last element
        self.heapify(0)  # heapify again
        return res  # and return the min element

    def decrease_key(self, i, x):
        """
        Time complexity: O(log n)

        Replace the key at index i with x and then we swap it with parent
        (and grant-parent etc) as needed till it's in its intended place.
        """
        arr = self.arr
        arr[i] = x  # replace the key at index i with x
        while i != 0 and arr[self.parent(i)] > arr[i]:  # bubble up
            p = self.parent(i)
            arr[p], arr[i] = arr[i], arr[p]
            i = p

    def delete(self, i):
        """
        Time complexity: O(log n)

        delete the key at index i and then use decreaseKey to make sure heap property is honoured.
        """
        if i >= len(self.arr):
            return
        else:
            # set the intended key to negative infinity. It will bubble up to root.
            self.decrease_key(i, -math.inf)
            self.extract_min()  # remove the root and re-heapify


"""
Heap Sort
    Can be seen as optimization over selection sort.
    In selection sort, we find out the maximum element in the array using linear search, swap it with the last
    continue with the remaining elements.
    The idea of heap sort is instead of doing a linear search, we maintain the remaining elements in heap structure.
    With heap data structure, we can find maximum or minimum in O(log n) time and therefore the overall complexity
    becomes O(n log n) rather than O(n^2) like selection sort.

Steps:
    1. Build a max heap
    2. Repeatedly swap root with the last node, reduce heap size by 1 and heapify

Time complexity: O(n log n)
Aux space: O(1) (or O(log n) if we use recursion)

It's not stable.
Heapsort is 2-3 times slower than quicksort because quicksort has better locality of reference than heapsort.
Used in hybrid sorting algorithms like IntroSort
"""


def build_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):  # starting from last non-leaf node
        max_heapify(arr, n, i)


def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[largest]:
        largest = left
    if right < n and arr[right] < arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)  # max_heapify the subtree with largest as its root


def heap_sort(arr):
    n = len(arr)
    build_heap(arr)
    # now that we have built the max heap with largest element at root i.e. 0th element of the array
    # swap it with last element of the array and reheapify the remaining part.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


class HeapTests(unittest.TestCase):
    def test_create_heap(self):
        heap = MinHeap([30, 20, 50, 10, 70, 60])
        print(heap.arr)


if __name__ == "__main__":
    unittest.main()
