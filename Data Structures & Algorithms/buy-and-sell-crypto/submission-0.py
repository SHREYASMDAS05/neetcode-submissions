class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        high_stock = prices[-1]
        for i in range(len(prices)-1 , -1 , -1):
            if prices[i] < high_stock:
                prof = high_stock - prices[i]
                res = max(prof , res)

            else:
                high_stock = prices[i]

        return res