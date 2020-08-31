"""
Find pair with given sum in the array.
eg: [1,2,3,4,5] = given sum 8 return 3, 5
Brut approach : Subtract every element from given sum and find the reminder value in array. This is in O n^2

Approach 1:
Create a dict of array elements and indices, enumerate array and so the same thing to return indices of sum.
Time comp. O(n) and space comp is O(n)

Approach 2:
Quick Sort array in sorted order and then take 2 counters from either ends. Add values at these two points and
check if < > than sum. Quick sort can be in n (log n) and comparisons will be in n which will be O(n log n)

"""
from DS.Sorting.QuickSort import *


def approach_2(a, tar):
    quickSort(a, 0, len(a) - 1)
    print(a)
    i = a[0]
    j = a[-1]
    while i <= j:
        if i + j < tar:
            i += 1
        if i + j > tar:
            j -= 1
        if i + j == tar:
            return i, j
    print("Elements not found")


def approach_1(arr, tar):
    sol = {}
    for i, val in enumerate(arr):
        if abs(tar - val) not in sol:
            sol[val] = i
        else:
            return [sol[tar - val], i]


def solve_brut(arr, tar):
    for i, val in enumerate(arr):
        if abs(tar - val) in arr and arr.index(abs(tar - val)) != i:
            return i, arr.index(abs(tar - val))
    print("Sum not found")


if __name__ == "__main__":
    arr = [12, 22, 20, 4]
    tar = 2
    sol = solve_brut(arr, tar)
    print("sol is", str(sol))
    print("------------------------")
    print(approach_2(arr, tar))