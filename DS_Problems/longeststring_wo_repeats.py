"""In given input find longest substring without repeat elements. If substrings with equal length return first substring """

class Solution:
    def lengthOfLongestSubstring(self, s):
        n = ""
        d = []
        c = 0
        for i in s:
            if i not in d:
                d.append(i)
                if len(n) <= len("".join(d)):
                    n = "".join(d)
            else:
                ind = d.index(i)
                del d[:ind + 1]
                d.append(i)
                if len(n) <= len("".join(d)):
                    n = "".join(d)
        return len(n)


S="yeihedgdgdddd"
s= Solution()
op = s.lengthOfLongestSubstring(S)
print(op)