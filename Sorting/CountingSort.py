"""
Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing).
Then doing some arithmetic to calculate the position of each object in the output sequence.
eg: Input data: 1, 4, 1, 2, 7, 5, 2
Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0   1  1  0  1  0  0
Counting sort runs in O(n)time, making it asymptotically faster than comparison-based sorting algorithms like quicksort or merge sort.
Counting sort only works when the range of potential items in the input is known ahead of time.
If the range of potential values is big, then counting sort requires a lot of space (perhaps more than O(n)).
https://www.interviewcake.com/concept/java/counting-sort

For numeric values its easier to create an array and manipulate the indices for values however for non numeric values,
we could use hashmaps.
"""