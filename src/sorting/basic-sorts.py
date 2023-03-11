import unittest

"""
Bubble sort
The idea is in each iteration we bubble the highest value to the end of list.
    1st iteration -> 0 elements in their right position
    2nd iteration -> last element in right position
    3rd iteration -> last 2 elements in right elements

Time complexity: O(n²)

Characteristics: in-place, stable
What is stable? If there are two elements with same value, their order is maintained after sorting.
"""


def bubble_sort(l):
    n = len(l)
    for i in range(n - 1):
        # if no swap happen, the list is sorted.
        swapped = False
        # why n - i - 1? because each iteration last some elements will be in right position
        # i = 0, no elements in right place
        # i = 1, last element in right place
        # i = 2, last 2 elements on right place
        # therefore we don't need to consider last (n-i-1) elements in comparison
        for j in range(n - i - 1):
            # j = 0, compare 0th and 1st element and swap if out of order and move to next iteration
            # j = 1, compare 1st and 2nd and swap if needed and move to next iteration
            # so basically, for each i, run the inner loop n-i-1 times
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if swapped is False:
            return


"""
Selection Sort:
    Time complexity: Θ(n²)
    Does less memory writes compared to quicksort and mergesort etc.
    (cyclesort is optimal for memory writes)
    It's the same basic idea for heap sort
    Not stable
    In-place

Basic idea is we find min element and put it in 0th position, we find second minimum and
put it in 1st position and so on.
"""


def selection_sort(l):
    n = len(l)
    for i in range(n - 1):
        min = i  # consider ith element as min to start with
        # Iterate on sublist from i+1 to end to find index of min element
        # i = 0, sublist will be 1st element to end
        # i = 1, sublist will be 2nd element to end and so on
        for j in range(i + 1, n):
            if l[j] < l[min]:
                min = j  # found new smaller element
        # move the min element to right position, i.e ith position
        l[i], l[min] = l[min], l[i]


"""
Insertion sort
    Time complexity:
        Θ(n²) worst case when array is reverse sorted,
        Θ(n) best case of already sorted array,
        So it's O(n²)
    Stable
    In-place
    Used in practice for small array in hybrid sort alorithms like Timsort (python) and Introsort (C++)

Idea:
We maintain two parts in the list: sorted and unsorted. We iterate on the list, put each
element at right position in sorted part, grow the sorted part and continue.
In the beginning, we consider l[0] as sorted part and start iteration from l[1].
"""


def insertion_sort(l):
    for i in range(1, len(l)):  # start iterating from 1st element
        x = l[i]
        # at beginning, j will be the last element in th sorted part of list
        # find the right position for x in the sorted part. Move all elements that are
        # greater than x to right to make space for x at right place.
        j = i - 1
        while j >= 0 and x < l[j]:
            l[j + 1] = l[j]
            j -= 1
        # at the end of above loop, j points to first smaller element than x,
        # so the slot for x is is at j+1.
        l[j + 1] = x


class SortTests(unittest.TestCase):
    def test_bubble_sort(self):
        l = [6, 4, 8, 3, 10]
        bubble_sort(l)
        self.assertListEqual(l, [3, 4, 6, 8, 10])

    def test_selection_sort(self):
        l = [6, 4, 8, 3, 10]
        selection_sort(l)
        self.assertListEqual(l, [3, 4, 6, 8, 10])

    def test_insertion_sort(self):
        l = [6, 4, 8, 3, 10]
        insertion_sort(l)
        self.assertListEqual(l, [3, 4, 6, 8, 10])


if __name__ == "__main__":
    unittest.main()
