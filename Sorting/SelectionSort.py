"""
Selection Sort is as easy as bubble sort. In this we iterate over the array and find a min/max value in each iteration.
We compare and swap other elements with this min value for each iteration.
Best Case : O(n^2)
Worst Case: O(n^2)
Average Case: O(n^2)
Similar to Bubble its not suitable for large arrays. It can be modified by adding an additional variable to reduce iterations.
"""

def SelectionSort(n):
    for i in range(0, len(n)):
        min = i
        swap = 0
        for j in range(i+1, len(n)):
            if n[j] < n[min]:
                n[j], n[min] = n[min], n[j]
                swap += 1
        if swap == 0:
            break


if __name__ == "__main__":
    # arr = [2,3,5,6,7,1,4]
    # arr = [1, 2, 3, 4, 5, 6]
    arr = [22,3,4,2,11,3]
    print("Array before sorting :" + str(arr))
    n = SelectionSort(arr)
    print("Array after sorting :" + str(arr))