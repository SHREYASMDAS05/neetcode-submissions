class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i , curr , total):
            if total == target:
                res.append(curr.copy())
                return 
            if total > target or i >=len(nums):
                return 
            #include the current and don't move the index
            curr.append(nums[i])
            dfs(i , curr, total + nums[i] )
            curr.pop()
            dfs(i + 1 , curr, total)

        dfs(0 , [], 0)
        return res