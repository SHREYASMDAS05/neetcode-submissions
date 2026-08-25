class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i , curr ):
            if i >= len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            dfs(i +1 , curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            dfs(i +1 , curr)

        dfs(0 , [])
        return res