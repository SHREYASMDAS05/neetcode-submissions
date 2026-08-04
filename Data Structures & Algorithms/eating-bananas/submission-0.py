class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_time(k):
            time =  0 
            for i in piles:
                time += (i + k -1) // k

            return time 

        l , r = 1 , max(piles)
        while l <= r:
            m = (l + r)//2
            time = total_time(m)
            if time <= h:
                r = m -1
            else:
                l = m + 1

        return l 

