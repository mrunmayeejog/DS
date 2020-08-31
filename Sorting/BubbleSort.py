"""
Bubble sort is the simplest sorting algorithm. In this the given array is iterated and in each iteration two elements are
compared and swapped. Thus in each iteration the largest/smallest element is put in its right place.

Best Case : O(n^2)
Worst Case: O(n^2)
Average Case: O(n^2)
Since it iterate always the time complexity is the same. Hence not suitable for large number of arrays.
This can be modified by keeping an additional swap counter.
If its 0 it means no swapping taken place and its already sorted.
"""

def BubbleSort(n):
    for each in n:
        swap = 0
        for i in range(0, len(n) - 1):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
                swap += 1
        if swap == 0:
            break

    return n

if __name__ =="__main__":
    # arr = [2,3,5,6,7,1,4]
    arr= [1,2,3,4,5,6]
    print("Array before sorting :" + str(arr))
    n = BubbleSort(arr)
    print("Array after sorting :" + str(arr))