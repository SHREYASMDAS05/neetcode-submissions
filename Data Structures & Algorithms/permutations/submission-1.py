class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                    continue

                used[i] = True
                curr.append(nums[i])

                dfs(curr)

                curr.pop()
                used[i] = False

        dfs([])
        return res