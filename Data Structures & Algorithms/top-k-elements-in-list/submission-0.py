from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         element_count = Counter(nums)
         print(element_count)
         element_count = sorted(element_count.items(), key = lambda x : x[1], reverse= True )
         return [elem for elem, freq in element_count[:k]]