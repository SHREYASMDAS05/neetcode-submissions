class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax , globalmin = nums[0] , nums[0]
        currmax , currmin = nums[0] , nums[0]
        total = nums[0]
        n = len(nums)
        for i in range(1 , n):
            currmax = max(nums[i] , currmax  + nums[i])
            currmin = min(nums[i] , currmin + nums[i])
            globalmax  = max(currmax , globalmax)
            globalmin = min(currmin , globalmin)
            total += nums[i]
        if globalmax >0:
            return max(total - globalmin , globalmax)
        else:
            return globalmax
        