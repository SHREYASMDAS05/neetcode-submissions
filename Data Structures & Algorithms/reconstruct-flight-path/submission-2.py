class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for src , desti in tickets:
            adj_list[src].append(desti)
        for src in adj_list:
            adj_list[src].sort(reverse=True)
        res = []
        def dfs(src):
            while adj_list[src]:
                dst = adj_list[src].pop()
                dfs(dst)

            res.append(src)
        dfs('JFK')
        return res[::-1]
