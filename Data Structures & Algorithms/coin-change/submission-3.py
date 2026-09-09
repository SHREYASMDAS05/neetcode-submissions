class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
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
        '''
        #tabulation
        dp = [float('inf')] * (amount + 1) #dp[amount] = min no coins required to make this amount 
        dp[0] = 0
        for i in range(1 , amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i]  = min(dp[i] ,1 + dp [i - coin ])

        return -1 if dp[amount] == float('inf') else dp[amount]

