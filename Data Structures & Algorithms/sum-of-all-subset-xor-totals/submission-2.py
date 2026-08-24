class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''def dfs(i , total):
            if i == len(nums):
                return total
                
            include = dfs(i + 1 , total ^ nums[i])
            exclude = dfs(i +1 , total)
            return  include + exclude

        return(dfs(0,0))'''
        res = 0
        for i in nums:
            res = res | i
        return res * (2**(len(nums)-1))