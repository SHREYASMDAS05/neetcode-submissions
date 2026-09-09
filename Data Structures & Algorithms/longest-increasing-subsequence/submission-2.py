class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i , prev):
            if i == len(nums):
                return 0 
            if (i , prev) in memo:
                return memo[(i,prev)]
            skip = dfs(i+1 , prev)
            take = 0 
            if nums[i] > nums[prev] or prev == -1:
                take = 1 + dfs(i+1 , i)
            memo[(i , prev)] = max(skip , take)
            return memo[(i , prev)]
        return dfs(0 , -1)
        