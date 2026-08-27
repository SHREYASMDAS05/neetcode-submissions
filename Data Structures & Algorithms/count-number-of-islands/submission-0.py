class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visited = [[0]*cols for i in range(rows)]
        que = deque()
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == '1':
                    que.append((r,c))
                    visited[r][c] = 1
                    while que:
                        r , c = que.popleft()
                        if r<rows-1 and grid[r+1][c] == '1' and not visited[r+1][c]:
                            que.append((r+1,c))
                            visited[r+1][c] = 1
                        if c<cols-1 and  grid[r][c+1] == '1' and not visited[r][c+1]:
                            que.append((r,c+1))
                            visited[r][c+1] = 1
                        if r>0 and grid[r-1][c] == '1' and not visited[r-1][c]:
                            que.append((r-1,c))
                            visited[r-1][c] = 1
                        if c>0 and  grid[r][c-1] == '1' and not visited[r][c-1]:
                            que.append((r,c-1))
                            visited[r][c-1] = 1

                    cnt +=1

        return cnt 

                    
