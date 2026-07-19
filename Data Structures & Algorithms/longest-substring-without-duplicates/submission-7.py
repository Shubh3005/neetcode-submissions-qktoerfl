class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        max_length=0
        p1= 0 
        for p2, l in enumerate(s):
            while l in contains:
                contains.remove(s[p1])
                p1+=1
            contains.add(l)
            max_length = max(max_length,p2-p1+1)

    
        return max_length