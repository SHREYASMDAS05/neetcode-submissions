class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0],0,0]] #time/mxheight , row , col
        visit.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while minH:
            time , r , c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return time 
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                if 0<= nr < N and 0<= nc <N and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    heapq.heappush(minH,[max(time , grid[nr][nc]), nr ,nc])

        