class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        #if buy -> i + 1
        #if sell -> i+2 considering hte cooldown day 
        def dfs(i, buying): #for purticular index I'm I buying it or not 
            if i >= len(prices):
                return 0 
            if (i , buying) in dp:
                return dp[(i , buying)]

            #if I'm buying it 
            if buying:
                buy = dfs(i+1 , not buying) - prices[i] #dfsof it gives totl profit possible then minusing from present number as we buying it 
                cooldown = dfs(i+1 , buying) 
                dp[(i,buying)] = max(buy , cooldown)
            else:
                sell = dfs(i+2 , not buying) + prices[i]
                cooldown = dfs(i+1 , buying)
                dp[(i,buying)] = max(sell , cooldown)
            return dp[(i , buying)]
        return dfs(0 , True)

        