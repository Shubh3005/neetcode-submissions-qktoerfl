from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {}
        for i in strs:
            key = tuple(sorted(Counter(i).items()))
            if key in d:
                d[key].append(i)
            else:
                d[key]= [i]
        res=[]
        for i in d.values():
            res.append(i)
        return res