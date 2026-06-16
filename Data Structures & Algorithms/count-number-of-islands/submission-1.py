class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        islands= 0
        def dfs(r,c):
            if 0<=r< rows and 0 <= c<cols and (r,c) not in visited and grid[r][c]=="1":
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        visited=set()        
        for r in range(rows):
            for c in range(cols):
                if(r,c) not in visited and grid[r][c]=="1":
                    islands+=1
                    dfs(r,c)
        return islands