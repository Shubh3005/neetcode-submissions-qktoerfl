class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if there is a cycle it is wrong
        #DFS again
        #Hash map to represent adjacency list
        # preMap 
        # 0 --> [1,2]
        # 1 --> [3,4]
        # 2 --> []
        # 3 --> [4]
        # 4 --> []
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet= set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True