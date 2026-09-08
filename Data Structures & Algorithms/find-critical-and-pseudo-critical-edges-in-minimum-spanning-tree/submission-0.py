class unionfind:
    def __init__(self ,n):
        self.par = [i for i in range(n)]
        self.rank = [1] *n 

    def find(self ,x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self ,x1 , x2):
        p1 , p2 = self.find(x1) , self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1]+= self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        for i , e in enumerate(edges):
            e.append(i) # to save the index after we sort also 
        edges.sort(key = lambda e:e[2])

        #kruskal's algo to find MST weight
        mst_weight = 0 
        uf = unionfind(n)
        for v1 , v2 , w , i in edges:
            if uf.union(v1 , v2):
                mst_weight += w
        #to check the critical and pseudo 
        critical , pseudo = [] , []

        for n1 , n2 , edge_weight , i in edges:
            weight = 0 
            uf = unionfind(n)
            for v1 , v2 , w , j in edges:
                if i!= j and uf.union(v1, v2):
                    weight += w

            if max(uf.rank) != n or weight > mst_weight :
                critical.append(i)
                continue
            #for pseudo 
            uf = unionfind(n)
            uf.union(n1 ,n2)
            weight = edge_weight
            for v1 , v2 , w , j in edges:
                if uf.union(v1,v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)

        return [critical , pseudo]
        