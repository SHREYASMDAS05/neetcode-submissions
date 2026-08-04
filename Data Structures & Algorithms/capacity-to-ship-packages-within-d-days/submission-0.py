class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysneeded(weight):
            day = 1
            current = 0 
            for i in weights:
                if current + i <= weight:
                    current += i
                else:
                    day +=1
                    current = i

            return day

        l , r = max(weights) , sum(weights)

        while l <= r:
            m = (l + r)//2
            day = daysneeded(m)
            
            if day <= days:
                r = m - 1

            else:
                l = m + 1

        return l  