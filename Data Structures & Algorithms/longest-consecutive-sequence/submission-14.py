class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       nums = set(nums)
       res=0
       highest= 0
       for i in nums:
            if i-1 not in nums:
                length = 1
                while i + length in nums:
                    length +=1
                res = max(res,length)
       return res
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # curr = 0
        # highest = 0
        # star
        # for i in range(1,len(nums)):
        #     if nums[i]>= num[i-1]:
        #         curr+=1
        #     if curr>highest:
        #         highest+=1
            