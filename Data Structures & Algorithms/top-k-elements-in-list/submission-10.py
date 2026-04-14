import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # top_k = count.most_common(k)
        # res=[]
        # for i, num in top_k:
        #     res.append(i)
        # return res

        #Bucket sort
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]= 1+ count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        