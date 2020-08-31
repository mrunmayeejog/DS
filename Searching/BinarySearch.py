"""
Binary Search works recursively on sorted list of array to find the given element.
"""

def binary_search(arr, low, high, val):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == val:
            return mid

        elif val <= arr[mid]:
            return binary_search(arr, low, mid - 1, val)

        elif val > arr[mid]:
            return binary_search(arr, mid + 1, high, val)


if __name__ == "__main__":
    data = [1,2,3,4,50,60,112,432]
    res = binary_search(data, 0, len(data), 11)
    if res:
        print("Element found at " + str(res))
    else:
        print("Element not found")