class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        # while l<r:
        #     mid = (l+r)//2
        #     if nums[mid] < nums[r]:
        #         r= mid
        #     else:
        #         l= mid+1
            
        # return nums[l]
        while l<r:
            mid= (l+r)//2
            if nums[mid-1]> nums[mid]:
                return nums[mid]
            elif nums[l]<= nums[mid] > nums[r]:
                l= mid+1
            else:
                r= mid-1
        return nums[l]
