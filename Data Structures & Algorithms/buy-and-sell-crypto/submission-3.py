class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0 
        for i in prices:
            if i< minPrice:
                minPrice= i
            else:
                maxPrice= max(maxPrice, i-minPrice)
        return maxPrice