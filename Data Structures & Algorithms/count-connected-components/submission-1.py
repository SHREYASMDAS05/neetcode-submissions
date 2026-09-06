class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        visited = [0] * n
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        cnt = 0 
        for i in range(n):
            if visited[i] == 1:
                continue
            cnt += 1
            visited[i] = 1 
            q= deque()
            q.append(i)
            while q:
                node = q.popleft()
                for children in graph[node]:
                    if visited[children] == 0:
                        visited[children] = 1
                        q.append(children)

        return cnt 