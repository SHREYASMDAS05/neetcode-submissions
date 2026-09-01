class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1) , (0,-1) , (1,0) , (-1 , 0)]
        rows , cols = len(grid) , len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    grid[r][c] = 0
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while q and fresh > 0 :
            for i in range(len(q)):
                r , c = q.popleft()
                for dr , dc in directions:
                    nr , nc = dr + r , dc + c

                    if 0 <= nr < rows and 0<= nc< cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 223
                        fresh -=1
                        q.append((nr,nc))
            time += 1

        return time if fresh == 0 else -1
                

        

