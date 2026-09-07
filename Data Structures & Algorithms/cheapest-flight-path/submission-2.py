class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n 
        prices[src] = 0
        for i in range(k +1):
            tempprices = prices.copy()
            for s , d , p in flights:
                if prices[s] == float('inf'): #if we can't reach the source
                    continue
                if prices[s] + p < tempprices[d]: #if the present cost to trvel to destination d is more than the present path 
                    tempprices[d] = prices[s] + p

            prices = tempprices

        return -1 if prices[dst] == float('inf') else prices[dst]
                
