class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                dfs(curr)
                curr.pop()
        dfs([])

        return res