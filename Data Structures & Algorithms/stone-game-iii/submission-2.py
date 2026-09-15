class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}

        def dfs(i):
            if i == len(stoneValue):
                return 0

            if i in memo:
                return memo[i]

            res = float('-inf')
            total = 0

            for j in range(i, min(i + 3, len(stoneValue))):
                total += stoneValue[j]
                res = max(res, total - dfs(j + 1))

            memo[i] = res
            return res

        score = dfs(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
            