class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,-1),(-1,0),(1,0),(0,1)]
        rows , cols = len(grid) , len(grid[0])
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==0: 
                    que.append((r,c))

        while que:
            r ,c = que.popleft()
            for dr , dc in directions:
                nr , nc = r + dr , c +  dc
                if 0<= nr <rows and 0<=nc<cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    que.append((nr,nc))

                

                            

