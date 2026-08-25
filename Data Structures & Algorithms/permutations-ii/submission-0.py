class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        def dfs(curr):
            if len(nums) == len(curr):
                res.append(curr.copy())
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                curr.append(nums[i])
                dfs(curr)
                curr.pop()
                used[i] = False

        dfs([])
        return res