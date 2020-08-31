"""
Part 1:
Check if subarray with 0 sum is exists or not.
eg : [3, 4,-7, 2, 4, 1,-2, 3, -1]
then subarrays  = [3,4,-7], [-7, 2, 4, 1], [-2, 3, -1] are present hence return True else false.

Brut Approach: For each index run a for loop to add sums and maintain a subarray and when the sum = 0 return the subarray.

Approach 1: This approach will not need sorting as it will change the array.
We can use hashing or dict to maintain the if sum has already encountered. But to return the exact the subarray.

Part 2:
Print all sub arrays with sum 0
"""


def approach_1(arr):
    s = []
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
        if sum == 0 or sum in s:
            return True
        s.append(sum)
    return False


def print_subarrays(arr):
    op = []
    for each in range(0, len(arr)):
        sum = 0
        sub_arr = []
        for i in range(each, len(arr)):
            sum += arr[i]
            sub_arr.append(arr[i])
            if sum == 0:
                op.append(sub_arr)
                break
    return op


if __name__ == "__main__":
    a = [3, 4, -7, 2, 4, 1, -2, 3, -1]
    # a = [0 , 1, -1, 0, 1, 0, 1, -1, -1, 1, 1]
    # op = brut_approach(a)
    op = print_subarrays(a)
    print(op)