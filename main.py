from random import randint
import time
import matplotlib.pyplot as plt

temp_insertion_results = []
temp_binary_insertion_results = []
temp_merge_results = []
temp_heap_results = []
temp_bubble_results = []
temp_selection_results = []
temp_quick_results = []
insertion_results = []
binary_insertion_results = []
merge_results = []
heap_results = []
bubble_results = []
selection_results = []
quick_results = []


def partition(start, end, array):

    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end

# The main function that implements QuickSort
def quick_sort(start, end, array):

    if (start < end):

        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


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


def selection_sort(arr):
    for i in range(len(arr)):

    # Find the minimum element in remaining
    # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

    # Swap the found minimum element with
    # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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
    temp_insertion_results.append(round(end-start, 5))


def test_binary_insertion_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    insertion_binary_sort(sort_arr)
    end = time.time()
    temp_binary_insertion_results.append(round(end-start, 5))


def test_merge_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    merge_sort(sort_arr)
    end = time.time()
    temp_merge_results.append(round(end-start, 5))


def test_heap_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    heap_sort(sort_arr)
    end = time.time()
    temp_heap_results.append(round(end-start, 5))


def test_bubble_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    bubble_sort(sort_arr)
    end = time.time()
    temp_bubble_results.append(round(end-start, 5))


def test_selection_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    selection_sort(sort_arr)
    end = time.time()
    temp_selection_results.append(round(end-start, 5))


def test_quick_sort(arr):
    sort_arr = arr.copy()
    start = time.time()
    quick_sort(0, len(sort_arr) - 1, sort_arr)
    end = time.time()
    temp_quick_results.append(round(end-start, 5))


def avgarr(arr):
    temp = 0
    for k in range(len(arr)):
        temp = temp + arr[k]
    return (round(temp / len(arr), 5))


def lowest(arr):
    temp = arr[0]
    for k in range(len(arr)):
        if temp > arr[k]:
            temp = arr[k]
    return (round(temp, 5))

if __name__ == "__main__":
    for i in range(10):
        for j in range(1):
            test_arr = gen_random_arr(i)
            test_insertion_sort(test_arr)
            test_binary_insertion_sort(test_arr)
            test_merge_sort(test_arr)
            test_heap_sort(test_arr)
            test_bubble_sort(test_arr)
            test_selection_sort(test_arr)
            test_quick_sort(test_arr)
        insertion_results.append(lowest(temp_insertion_results))
        binary_insertion_results.append(lowest(temp_binary_insertion_results))
        merge_results.append(lowest(temp_merge_results))
        heap_results.append(lowest(temp_heap_results))
        bubble_results.append(lowest(temp_bubble_results))
        selection_results.append(lowest(temp_selection_results))
        quick_results.append(lowest(temp_quick_results))
        temp_insertion_results = []
        temp_binary_insertion_results = []
        temp_merge_results = []
        temp_heap_results = []
        temp_bubble_results = []
        temp_selection_results = []
        temp_quick_results = []

    print("Insertion Sort Results: " + str(insertion_results))
    print("Binary Insertion Sort Results: " + str(binary_insertion_results))
    print("Merge Sort Results: " + str(merge_results))
    print("Heap Sort Results: " + str(heap_results))
    print("Bubble Sort Results: " + str(bubble_results))
    print("Selection Sort Results: " + str(selection_results))
    print("Quick Sort Results: " + str(quick_results))

    count = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    plt.plot(count, insertion_results, label="Insertion")
    plt.plot(count, binary_insertion_results, label="Binary Insertion")
    plt.plot(count, merge_results, label="Merge")
    plt.plot(count, heap_results, label="Heap")
    plt.plot(count, bubble_results, label="Bubble")
    plt.plot(count, selection_results, label="Selection")
    plt.plot(count, quick_results, label="Quick")
    plt.xlabel("Numbers In List")
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()
