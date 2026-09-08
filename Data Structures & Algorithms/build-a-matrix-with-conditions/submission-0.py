class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src , adj , visit , path , order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei , adj , visit , path , order):
                    return False
            path.remove(src)
            order.append(src)
            return True
        
        def topo_sort(edges):
            adj = defaultdict(list)
            for src , dst in edges:
                adj[src].append(dst)

            visit , path = set() , set()
            order = []
            for src in range(1 , k+1):
                if not dfs(src , adj , visit , path , order):
                    return []
            return order[::-1]

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if not row_order or not col_order:
            return []
        val_to_row = {n:i for i , n in enumerate(row_order)}
        val_to_col = {n:i for i , n in enumerate(col_order)}

        res = [[0]*k for i in range(k)]
        for num in range(1 ,k+1):
            r , c = val_to_row[num] , val_to_col[num]
            res[r][c] = num

        return res