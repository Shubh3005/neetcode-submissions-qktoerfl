class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols=len(heights), len(heights[0])
        pac,atl= set(),set()
        res=[]
        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or r<0 or c<0 or r==rows or c == cols or heights[r][c] <prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for i in range(cols):
            dfs(0,i,pac,heights[0][i])
            dfs(rows-1, i, atl, heights[rows-1][i])
        for j in range(rows):
            dfs(j, 0,pac,heights[j][0])
            dfs(j,cols-1,atl,heights[j][cols-1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res