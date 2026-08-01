class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        l , r = 0 , 1
        while r < len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                res = max(prof , res)
            else:
                l = r
            r+=1

        return res