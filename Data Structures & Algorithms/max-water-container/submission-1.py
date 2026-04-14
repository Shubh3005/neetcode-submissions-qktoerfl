class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxarea= 0
        while l<r:
            length = r-l
            maxarea= max(length*min(heights[l],heights[r]), maxarea)
            if heights[l]<heights[r] and l<r:
                l+=1
            elif heights[r]<=heights[l] and l<r:
                r-=1
        return maxarea
        