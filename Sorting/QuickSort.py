"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm.
It picks an element as pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways.
-Pick first element as pivot.
-Pick last element as pivot.
-Pick a random element as pivot.
-Pick median as pivot.

The main process is partition() which is responsible for finding pivot and dividing the array.
The partitioning takes place by dividing the array by 2 at each level.
Hoare's method: We start with two counters i and j from each end and compare and move these counters towards each other.

Best case = O (n log n) when the pivot is approx closer to the actual median.
Worst Case = O ( n ^ 2) when is the list already in sorted order.

Space complexity = O (log n) to O(n) Size of the stack depends on height of the tree.
"""

c = 0
d = 0

def partition_first(arr, low, high):
    global c
    # Pivot as first element  with Hoarse' Method
    pivot = arr[low]
    i = low
    j = high
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            c += 1
    return i


def partition_last(arr, low, high):
    # Lomuto's method with last element as pivot
    i = low
    pivot = arr[high]
    global d
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            d += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def partition_at_middle(arr, low, high):
    pivot = (low + high) // 2
    i = low
    j = high
    while i <= j:
        while arr[i] < arr[pivot]:
            i += 1
        while arr[j] > arr[pivot]:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i


def partition_first_lomuto(arr, low, high):
    # Lomuto's method with first element as pivot
    pivot = low  # pivot
    i = low + 1  # a variable to memorize where the
    # partition in the array starts from.
    for j in range(low + 1, high + 1):

        # if the current element is smaller or equal to pivot,
        # shift it to the left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return (pivot)
    # change the quicksort ranges to i - 1 and i + 1


def quickSort(arr, low, high):
    if low < high:
        # i = partition_first(arr, low, high)
        # i = partition_last(arr, low, high)
        i = partition_at_middle(arr, low, high)
        quickSort(arr, low, i - 1)
        quickSort(arr, i , high)


if __name__ == "__main__":
    a = [10, 23, 4, 56, 233, 5, 6, 74]
    print("Before sorting: " + str(a), end="")
    quickSort(a, 0, len(a) - 1)
    print("\nAfter sorting: " + str(a), end="")
    print("\n" + str(d))