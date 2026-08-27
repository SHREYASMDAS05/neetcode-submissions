class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        town_judge = trust[0][1]
        visited = [0] * (n+1)
        for u , v in trust:
            if not visited[u]:
                if v != town_judge:
                    return -1
                if u == town_judge:
                    return -1
                visited[u] =1

        return town_judge