class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numComp= {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numComp:
                return [numComp[comp], i]
            numComp[nums[i]] = i
        return []