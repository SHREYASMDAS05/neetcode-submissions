class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total //2
        if sum(nums) % 2 != 0:
            return False
        memo = {}
        def dfs( i , curr):
            if curr == target:
                return True
            if  i == len(nums) or curr > target:
                return False
            if (i , curr) in memo:
                return memo[(i,curr)]
            #take
            take = dfs(i+1 , nums[i] + curr)
            #skip
            skip = dfs(i+1 , curr)
            memo[(i,curr)] = skip or take
            return memo[(i , curr)]

        return dfs(0 , 0)
