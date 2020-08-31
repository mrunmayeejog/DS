"""
Solving this example with modified binary search.
part_x = start + len(small_arr) // 2 (floor div)
part_x + part_y = len(x) + len(y) + 1 / 2 -> total_len
part_y = total_len = part x

if small_arr[partx-1] < large_arr[party] and small_arr[partx] > large_arr[party -1]
    if odd len: then max(small_arr[partx-1], large_arr[party -1])
    else return avg(max(small_arr[partx-1], large_arr[party -1])) + min(small_arr[partx],large_arr[party])
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            arr_s = nums1
            arr_l = nums2
        else:
            arr_s = nums2
            arr_l = nums1
        start, end = 0, len(arr_s)
        part_len = int((len(arr_l) + len(arr_s) + 1) / 2)
        while True:
            part_x = (start + end) // 2
            part_y = part_len - part_x
            # print(part_x, part_y)
            # print("  " + str(arr_s[0:part_x]) + "      |     " + str(arr_s[part_x:]))
            # print("  " + str(arr_l[0:part_y]) + " | " + str(arr_l[part_y:]))
            xi = float('-inf') if part_x == 0 else arr_s[part_x - 1]
            xj = float('inf') if part_x == len(arr_s) else arr_s[part_x]
            yi = float('-inf') if part_y == 0 else arr_l[part_y - 1]
            yj = float('inf') if part_y == len(arr_l) else arr_l[part_y]

            if xi <= yj:
                if xj >= yi:
                    if (len(arr_l) + len(arr_s)) % 2 == 0:
                        return (max(xi, yi) + min(xj, yj)) / 2
                    return max(xi, yi)
                else:
                    start = part_x + 1
                    end = end
            else:
                start = start
                end = part_x


if __name__ == "__main__":
    a1 = [2, 12, 30, 33, 45]
    a2 = [1, 12, 20, 24, 25]
    s = Solution()
    n = s.findMedianSortedArrays(a1, a2)
    print(n)