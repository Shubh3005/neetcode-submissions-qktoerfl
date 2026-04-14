class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice= prices[0]
        maxProft= 0
        for i in prices:
            if i<minprice:
                minprice= i
            else:
                print(maxProft)
                maxProft = max(maxProft, i-minprice)
        return maxProft

