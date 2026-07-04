# from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res = []
        for i in strs:
            if "".join(sorted(i)) in dic:
                dic["".join(sorted(i))].append(i)
            else:
                dic["".join(sorted(i))]= [i]
        for i in dic:
            res.append(dic[i])
        return res
        
        
        
        
        
        
        # dictionary = {}
        # res= []
        # for i in strs:
        #     print(sorted(i))
        #     if "".join(sorted(i)) in dictionary:
        #         dictionary["".join(sorted(i))].append(i)
        #     else:
        #         dictionary["".join(sorted(i))]= [i]
        # for i in dictionary:
        #     res.append(dictionary[i])
        # print(dictionary)
        # return res

        
        
        
        
        
        
        
        
        # # lst = defaultdict(list)
        # # for s in strs:
        # #     key = tuple(sorted(s))
        # #     lst[key].append(s)
        # # return list(lst.values())
        # # # res = []
        # # # for s in strs:
        # # #     placed = False
        # # #     for group in res:
        # # #         if Counter(s) == Counter(group[0]):
        # # #             group.append(s)
        # # #             placed = True
        # # #             break

        # # #     if not placed:
        # # #         res.append([s])

        # # # return res
                 
