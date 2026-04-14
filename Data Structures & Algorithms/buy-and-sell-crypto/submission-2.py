class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice= prices[0]
        maxprofit=0
        for i in prices:
            minprice= min(i, minprice)
            maxprofit = max(i-minprice,maxprofit)
           
        return maxprofit