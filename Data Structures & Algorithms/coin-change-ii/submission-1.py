class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        chache = {}
        def dfs(i , a):
            if a == amount:
                return 1
            if a > amount:
                return 0 
            if i >= len(coins):
                return 0 
            if (i , a) in chache:
                return chache[(i,a)]

            chache[(i,a)] = dfs(i , a + coins[i]) + dfs(i +1 , a)
            return chache[(i,a)]
        return dfs(0 , 0)
        '''
        dp = [[0]* (len(coins)+1) for i in range(amount+1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range( 1,amount + 1):
            for i in range(len(coins) - 1 , -1 , -1):
                dp[a][i] = dp[a][i+1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a-coins[i]][i]
        return dp[amount][0]

        
         