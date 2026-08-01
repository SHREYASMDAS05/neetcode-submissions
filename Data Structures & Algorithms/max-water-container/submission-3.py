class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        res = 0
        while l < r:
            water = (r -l) * min(heights[l] , heights[r])
            res= max(water , res)

            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:#if both are same shift either
                r-=1
        return res
