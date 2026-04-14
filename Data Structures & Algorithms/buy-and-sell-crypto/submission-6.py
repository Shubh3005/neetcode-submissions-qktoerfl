class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice= float("inf")
        maxProf = 0
        for i in prices:
            if i <minPrice:
                minPrice = i
            else:
                maxProf= max(maxProf, i-minPrice)
        return maxProf