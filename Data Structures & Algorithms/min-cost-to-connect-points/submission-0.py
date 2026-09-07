class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(points)
        for i in range(N):
            x1 , y1 = points[i]
            for j in range(i+1 , N):
                x2 , y2 = points[j]
                cost = abs(x1-x2) + abs(y1 - y2)
                adj[i].append([cost , j])
                adj[j].append([cost ,i])

        #prims algorithm 
        res = 0 
        minH = [[0,0]] #cost , point
        visit = set()
        while len(visit) < N:
            cost , node = heapq.heappop(minH)
            if node in visit:
                continue
            visit.add(node)
            res += cost
            for neighcost , nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH , [neighcost , nei])

        return res
