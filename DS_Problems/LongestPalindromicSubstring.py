class Solution:
    def __init__(self):
        self.counter = {}
        self.string = ""
        self.output = ""

    def check(self, arr):
        print("................" + str(arr))
        if len(arr) <= 1:
            return arr
        if len(arr) == 2 and arr[0] == arr[1]:
            return arr
        arr = self.palindrome_str(0, arr[0], arr)
        return arr

    def palindrome_str(self, ind, letter, arr):
        j = len(arr) - 1
        print(arr,j)
        i = 0
        bool = False
        while j > 0:
            if letter == arr[j]:
                print("________________________________________________________________" + str(arr[j]))
                print(j, arr, ind, letter)
                c = self.check(arr[i+1:j])
                if c:
                    print("aaaaaaaaaaaaaaa<<<<<<<<" + str(arr))
                    # arr = self.palindrome_str(ind+1, arr[ind+1], arr[ind+1:j])
                    if len(self.output) < len("".join(arr)):
                        self.output = "".join(arr)
                        print("***************" + str(self.output))
            j -= 1
            i += 1
        return self.output

    def longestPalindrome(self, s: str) -> str:
        self.string = s
        for i, val in enumerate(self.string):
            if val in self.counter:
                self.counter[val].append(i)
            else:
                self.counter[val] = [i]
        print(self.counter)
        print("Input - " +str(self.string))

        for ele in self.counter:
            if len(self.counter[ele]) > 1:
                print("element " + str(ele))
                ind = self.counter[ele][0]
                letter = self.string[ind]
                ps = self.palindrome_str(ind, letter, self.string[ind:])

        if len(self.output) > 0:
            print("Palindrome found " +str(self.output))
            return self.output
        else:
            print("Palindrome not found")
            return self.string[0]



if __name__ == "__main__":
    s = "jogmadamjog"
    c = Solution()
    op = c.longestPalindrome(s)
    print(op)