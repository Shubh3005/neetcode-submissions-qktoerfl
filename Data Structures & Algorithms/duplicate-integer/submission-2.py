class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = []
        for i in nums:
            if i not in set:
                set.append(i)
            else:
                return True
        return False
            