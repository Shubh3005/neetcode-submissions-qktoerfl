class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxA= 0
        while l<r:
            length = r-l
            maxA= max(maxA, (min(heights[l],heights[r])*length))
            if heights[l]<=heights[r] and l<r:
                l+=1
            elif heights[r]< heights[l] and l<r:
                r-=1
            
        return maxA