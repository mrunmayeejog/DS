"""
Merge Sort is a Divide and Conquer algorithm.
It divides the input array in two halves, calls itself for the two halves and then merges the two sorted halves.
The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted
and merges the two sorted sub-arrays into one.

Space Complexity : O(n)
Time complexity:

Time complexity of Merge Sort is Theta(n Log n) in all 3 cases (worst, average and best)
as merge sort always divides the array into two halves and take linear time to merge two halves.

In Merge the divide part takes the time complexity of log n.
Example if you have 5 arrays [1,2,3,4,5] then
first level has l = 2 ele -> [1,2] R = 3 ele -> [3,4,5]
Second level Branch 11 : L= 1 ->[1] ele R = 1 ->[2] ele Branch 12: L= 1 ele -> [3] R= 2 ele ->[4,5]
Third Level Branch 12: Further divided into - Branch 21: l=1 [4] R = 1 [5]

Thus partitioning takes place in log n time and merging takes place in n comparisons.
"""


def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)  # Sorting the first half ie go till the very last element and when returns do the same for R
        MergeSort(R)  # Sorting the second half
        merge(L, R, arr)


def merge(L, R, arr):
    i = j = k = 0
    # Compare each element from L and  R place it in a sorted way in the same array in sorted indices.
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


if __name__ == "__main__":
    # arr = [2,3,5,6,7,1,4]
    # arr = [1, 2, 3, 4, 5, 6]
    a = [22,13,4,2,11,3]
    print("Array before sorting :" + str(a))
    MergeSort(a)
    print("Array after sorting :" + str(a))
