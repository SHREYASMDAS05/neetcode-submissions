class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            currsum = 0 
            subarr = 0 
            for n in nums:
                currsum += n
                if currsum > largest:
                    subarr +=1
                    currsum = n
            
            return subarr + 1 <= k

        l , r = max(nums) , sum(nums)
        while l <= r:
            m = (l + r) // 2
            if cansplit(m):
                res = m
                r = m -1 

            else:
                l = m + 1

            
        return res