class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(heights)
        cols = len(heights[0])
        effort_arr = [[float('inf') for i in range(cols)] for i in range(rows)]
        effort_arr[0][0] = 0
        priority_que = [[0,0,0]] #to have effort , i , j
        while priority_que:
            eff , i , j = heapq.heappop(priority_que)
            if i == rows -1 and j == cols -1 :
                return eff
            for dr , dc in directions:
                nr , nc = i + dr , j + dc
                if 0<= nr<rows and 0 <= nc <cols:
                    new_eff = max(eff , abs(heights[nr][nc] - heights[i][j]))
                    if new_eff < effort_arr[nr][nc]:
                        effort_arr[nr][nc] = new_eff
                        heapq.heappush(priority_que ,[new_eff , nr , nc])

