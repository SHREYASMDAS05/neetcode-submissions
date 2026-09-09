class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0 :
                return 0 
            if amount < 0 :
                return float('inf')
            if amount in memo:
                return memo[amount]

            memo[amount] = float('inf')
            for coin in coins:
                memo[amount] = min(memo[amount] , 1 + (dfs(amount - coin)))

            return memo[amount]
        ans = dfs(amount)

        return -1 if ans == float('inf') else ans