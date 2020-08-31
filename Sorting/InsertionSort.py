"""
Insertion sort is again a simple sorting algorithm. In this we start iterating for length of arr and
for each key move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position.
Insertion Sort is very simple and intuitive to implement, which is one of the reasons it's generally taught at an early stage in programming.
It's a stable, in-place algorithm, that works really well for nearly-sorted or small arrs.
Insertion sort may seem like a slow algorithm for larger data sets due to its its O(n2) time complexity.
However, as we've mentioned, it's very efficient on small arrays and on nearly sorted arrays eg size less than 10
Insertion sort is a stable sort with a space complexity of O(1) due to inplace replacements.


Time complexities:
Best Case : O(n) if array is already in sorted order.
Worst Case: O(n^2)
Average Case: O(n^2)
"""


def InsertionSort(arr):
    # We start from 1 since the first element is sorted
    for i in range(1, len(arr)):
        cv = arr[i]
        cp = i
        print("Current " + str(cv))
        print("Current position " + str(cp))
        # We start with comparing current position till the beginning element in backwards order.
        # while checking theta te previous element is greater than cur value and index is > 0.
        # If yes move the larger element to the right. Till all the large elements are moved.
        # if the condition breaks it means one ele is less than curr. Then simple replace cur pos ele by cv.
        while cp > 0 and arr[cp - 1] > cv:
            arr[cp] = arr[cp -1]
            cp = cp - 1
            print(arr)

        arr[cp] = cv
        print("Sorted arr " + str(arr))
        print("\n")



if __name__ == "__main__":
    # arr = [2,3,5,6,7,1,4]
    # arr = [1, 2, 3, 4, 5, 6]
    arr = [22,3,4,2,11,3]
    print("Array before sorting :" + str(arr))
    n = InsertionSort(arr)
    print("Array after sorting :" + str(arr))