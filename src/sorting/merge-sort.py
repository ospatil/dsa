import unittest

"""
Merge two sorted lists
i/p: a = [10, 15, 20], b = [5, 6, 6, 30]
o/p: [5, 6, 6, 10, 15, 20, 30]
"""

# Time complexity: O((m+n) * log(m+n)) where m = len(a) and n = len(b)
# This solution doesn't use the fact that both lists are sorted
def merge_naive(a, b):
    res = a + b  # concatenate two lists
    res.sort()  # sort
    return res


# Time Complexity: Θ(m+n)
def merge_lists(a, b):
    res = []
    m, n = len(a), len(b)
    i = j = 0
    while i < m and j < n:  # run till we exhaust one of the lists
        if a[i] < b[j]:  # if element in a is smaller
            res.append(a[i])  # copy to result
            i += 1  # and move to the next element in a
        else:  # element in b is smaller
            res.append(b[j])  # copy to result
            j += 1  # and move to the next element in b
    # at this point one of the list is exhausted, so copy the remaining elements
    # from the list still having elements into the result.
    res.extend(a[i:])
    res.extend(b[j:])
    return res


"""
Merge subarrays
i/p: a = [10, 15, 20, 11, 13], low = 0, high = 4, mid = 2
o/p: [10, 11, 13, 15, 20]

i/p: a = [5, 8, 12, 14, 7], low = 0, high = 4, mid = 3
o/p: [5, 7, 8, 12, 14]

The elements from low to mid are sorted and so are elements from mid+1 to high.
We need to merge all elements from low to high in the same list and get all elements sorted.
Low <= mid < high

Implementation idea
Copy elements from low to mid into an auxiliary list called left.
Copy the elements from mid+1 to high into the aux list called right.
Merge left and right using the merge function like above.
"""


def merge(a, low, mid, high):
    # mid+1 to include mid in left and high+1 to include high in right
    left, right = (a[low : mid + 1], a[mid + 1 : high + 1])
    i = j = 0
    # k is the index in the list where we start appending the elements from the right list.
    k = low
    while i < len(left) and j < len(right):
        ## continue till one of the lists is exhausted
        if left[i] <= right[j]:
            # pick element from left. the equal to condition ensure stable merge process
            a[k] = left[i]  # copy into a
            i += 1  # move to next element in left
        else:  # pick element from right
            a[k] = right[j]  # copy into a
            j += 1  # move to next element in right
        k += 1  # increment k so that it points to next slot in a
    # at this point, one of the list is exhausted, copy remaining elements from other list
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


"""
Mergesort
Time complexity:
At each invocation, we split the input into 2 parts and make recursive calls.
Therefore, there height of recurrence tree will be O(log n) and at each level,
the work we do is merging the sorted parts i.e. Θ(n) work.
Therefore time complexity = O(n * log n)

Auxiliary space: O(n) for merge function
"""


def merge_sort(a, l, r):
    if r > l:  # # there should be at least 2 elements in the list to sort
        m = (r + l) // 2  # calculate mid-point
        merge_sort(a, l, m)  # recursively sort the left list
        merge_sort(a, m + 1, r)  # recursively sort the right list
        merge(a, l, m, r)  # merge two sorted lists


class MergeSortTests(unittest.TestCase):
    def test_merge_lists(self):
        self.assertListEqual(
            merge_lists([10, 15, 20], [5, 6, 6, 30]), [5, 6, 6, 10, 15, 20, 30]
        )

    def test_merge(self):
        a = [10, 15, 20, 11, 13]
        low, mid, high = 0, 2, 4
        merge(a, low, mid, high)
        self.assertListEqual(a, [10, 11, 13, 15, 20])
        a = [5, 8, 12, 14, 7]
        low, mid, high = 0, 3, 4
        merge(a, low, mid, high)
        self.assertListEqual(a, [5, 7, 8, 12, 14])

    def test_merge_sort(self):
        a = [10, 5, 30, 15, 7]
        merge_sort(a, 0, len(a) - 1)
        self.assertListEqual(a, [5, 7, 10, 15, 30])


if __name__ == "__main__":
    unittest.main()
