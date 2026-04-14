from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        d=defaultdict(list)

        for i, count in counter.items():
            d[count].append(i)
        
        count = [-count for count in d.keys()]
        heapq.heapify(count)
        res=[]
        for i in range(len(count)):
            next_count= - heapq.heappop(count)
            for i in d[next_count]:
                if len(res)==k:
                    return res
                res.append(i)
        return res
        
        
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # freq = {}
        # for i in nums:
        #     if i in freq:
        #         freq[i] +=1 
        #     else:
        #         freq[i] = 1
        # return sorted(freq, key=freq.get, reverse=True)[:k]
