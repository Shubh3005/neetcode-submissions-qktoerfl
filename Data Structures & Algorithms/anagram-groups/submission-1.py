from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for s in strs:
            placed = False
            for group in res:
                if Counter(s) == Counter(group[0]):
                    group.append(s)
                    placed = True
                    break

            if not placed:
                res.append([s])

        return res
                 
