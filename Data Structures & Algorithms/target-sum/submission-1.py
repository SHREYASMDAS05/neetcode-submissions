class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i , cursum):
            if i == len(nums):
                return 1 if cursum == target else 0
            if (i , cursum) in memo:
                return memo[(i , cursum)]
            
            memo[(i,cursum)] = dfs(i+1 , cursum + nums[i]) + dfs(i+1 , cursum - nums[i])
            return memo[(i,cursum)]
        return dfs(0 ,0)