class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0 , 0 
        length = float('inf')
        prefix = 0
        while r < len(nums):
            prefix += nums[r]
            while prefix  >= target:
                window = r - l + 1
                length = min(length , window)
                prefix -= nums[l]
                l+=1  
            r+=1

        return 0 if length == float('inf') else length