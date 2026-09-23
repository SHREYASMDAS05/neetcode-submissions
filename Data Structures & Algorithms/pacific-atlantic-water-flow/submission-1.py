class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights) , len(heights[0])
        pacific , atlantic = set() , set()
        directions = [(0,1) , (0,-1) , (1 ,0) , (-1 , 0)]
        def canreach(r ,c , visited , prevheight):
            if (r,c) in visited or r<0  or r == rows or c<0 or c== cols or heights[r][c] < prevheight:
                return
            visited.add((r,c))
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                canreach(nr , nc , visited , heights[r][c])

        for c in range(cols):
            canreach(0,c,pacific , heights[0][c])
            canreach(rows -1 , c ,atlantic , heights[rows -1 ][c])

        for r in range(rows):
            canreach(r , 0 , pacific , heights[r][0])
            canreach(r , cols-1 ,atlantic, heights[r][cols-1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
