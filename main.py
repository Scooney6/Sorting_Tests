from random import randint
import time
import matplotlib.pyplot as plt

insertion_results = []
binary_insertion_results = []
merge_results = []
heap_results = []
bubble_results = []


def insertion_sort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Python program for implementation of MergeSort
def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def binary_search(arr, val, start, end):

    # we need to distinugish whether we
    # should insert before or after the
    # left boundary. imagine [0] is the last
    # step of the binary search and we need
    # to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    # this occurs if we are moving
    # beyond left's boundary meaning
    # the left boundary is the least
    # position to find a number greater than val
    if start > end:
        return start

    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid


def insertion_binary_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


def gen_random_arr(num):
    arr = []
    if num == 0:
        for i in range(1000):
            arr.append(randint(0, 50000))
    else:
        for i in range((num+1) * 1000):
            arr.append(randint(0, 50000))
    return arr


def test_insertion_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    insertion_sort(sort_arr)
    end = time.time()
    insertion_results.append(float(str(end-start)[0:6]))


def test_binary_insertion_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    insertion_binary_sort(sort_arr)
    end = time.time()
    binary_insertion_results.append(float(str(end-start)[0:6]))


def test_merge_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    merge_sort(sort_arr)
    end = time.time()
    merge_results.append(float(str(end-start)[0:6]))


def test_heap_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    heap_sort(sort_arr)
    end = time.time()
    heap_results.append(float(str(end-start)[0:6]))


def test_bubble_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    bubble_sort(sort_arr)
    end = time.time()
    bubble_results.append(float(str(end-start)[0:6]))

if __name__ == "__main__":

    for i in range(8):
        test_arr = gen_random_arr(i)
        test_insertion_sort(test_arr)
        test_binary_insertion_sort(test_arr)
        test_merge_sort(test_arr)
        test_heap_sort(test_arr)
        test_bubble_sort(test_arr)
    print("Insertion Sort Results: " + str(insertion_results))
    print("Binary Insertion Sort Results: " + str(binary_insertion_results))
    print("Merge Sort Results: " + str(merge_results))
    print("Heap Sort Results: " + str(heap_results))
    print("Bubble Sort Results: " + str(bubble_results))

    count = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    plt.plot(count, insertion_results, label="Insertion")
    plt.plot(count, binary_insertion_results, label="Binary Insertion")
    plt.plot(count, merge_results, label="Merge")
    plt.plot(count, heap_results, label="Heap")
    plt.plot(count, bubble_results, label="Bubble")
    plt.xlabel("Numbers In List")
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()
