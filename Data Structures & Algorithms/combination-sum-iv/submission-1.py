class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0 
        memo = {}
        def dfs(curr):
            if curr > target:
                return 0 
            if curr == target:
                return 1
            res = 0
            if curr in memo:
                return memo[curr]
            for num in nums:
                res += dfs(curr + num)
            memo[curr] = res
            return memo[curr]

        return dfs(0)