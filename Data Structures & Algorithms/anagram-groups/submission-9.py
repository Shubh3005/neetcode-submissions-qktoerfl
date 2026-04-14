from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            val = tuple(sorted(Counter(i).items()))
            if val in d:
                d[val].append(i)
            else:
                d[val] = [i]
        res = []
        for i in d.values():
            res.append(i)
        return res
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # # d= {}
        # # for i in strs:
        # #     key = tuple(sorted(Counter(i).items()))
        # #     if key in d:
        # #         d[key].append(i)
        # #     else:
        # #         d[key]= [i]
       
        # # return list(d.values())

        # hm = collections.defaultdict(list)
        # for i in strs:
        #     s = str(sorted(list(i)))
        #     hm[s].append(i)
        # return list(hm.values())