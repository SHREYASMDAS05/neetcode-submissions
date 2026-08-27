class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visited = [[0] * cols for i in range(rows)]
        area = 0
        que = deque()
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for r in range(rows):
            for c in range(cols):
                subarea = 0
                if grid[r][c] == 1 and not visited[r][c]:
                    visited[r][c] = 1
                    subarea +=1
                    que.append((r,c))
                    while que:
                        r , c = que.popleft()
                        for dr , dc in dirs:
                            nr , nc = r + dr , c + dc
                            if 0<=nr<rows and 0<=nc < cols and grid[nr][nc] ==1 and not visited[nr][nc]:
                                visited[nr][nc] = 1
                                que.append((nr,nc))
                                subarea+=1

                area = max(area , subarea)


        return area


                    