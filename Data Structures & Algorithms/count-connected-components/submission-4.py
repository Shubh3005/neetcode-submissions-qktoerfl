class Union:
    def __init__(self, n):
        self.par = list(range(n)) #at first every node is a root node
        self.rank = [0] * n

    def union(self, node1, node2):
        r1, r2= self.find(node1), self.find(node2)
        if r1 == r2:
            return
        elif self.rank[r1]>self.rank[r2]:
            self.rank[r1]+=1
            self.par[r2]=r1
        else:
            self.rank[r2]+=1
            self.par[r1]=r2
    def find(self,node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u= Union(n)

        for x,y in edges:
            u.union(x,y)
            
        return len([i for i in range(n) if i == u.par[i]])