class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        length = 0
        p1 = 0 
        for p2, i in enumerate(s):
            while i in curr:
                curr.remove(s[p1])
                p1+=1
            curr.add(i)
            length = max(length, len(curr))
        return length

