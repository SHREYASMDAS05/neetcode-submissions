class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for n1 , n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        leaves = deque()
        for src , neigh in adj.items():
            if len(neigh) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neigh)

        while leaves:
            if n <=2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for neighbours in adj[node]:
                    edge_cnt[neighbours] -=1
                    if edge_cnt[neighbours] == 1:
                        leaves.append(neighbours)

