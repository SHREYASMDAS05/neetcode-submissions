class Solution:
    def candy(self, ratings: List[int]) -> int:
        summ = 1 
        i = 1 
        n = len(ratings)
        while i<n :
            #constant neighbour
            if ratings[i] == ratings[i-1]:
                summ += 1
                i+=1
                continue
            peak = 1
            #increasing neighbour
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                summ += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                summ += down
                i+=1
                down +=1
            if down > peak :
                summ += down - peak
        return summ

