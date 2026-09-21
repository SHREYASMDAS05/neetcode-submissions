class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        '''
        dp = {}
        def dfs(idx , jump):
            if idx >= n-1:
                return jump
            if (idx , jump) in dp:
                return dp[(idx , jump)]
            mini = float('inf')
            for i in range(1 , nums[idx] + 1):
                mini = min(mini , dfs(idx + i , jump + 1))
            dp[(idx ,jump)] = mini
            return mini
        return dfs(0 , 0)
        '''
        l , r = 0 , 0 
        jump = 0 
        while r < len(nums) - 1:
            farthest = 0 
            for i in range(l , r+1):
                farthest = max(farthest , i + nums[i])
            l = r+1
            r = farthest 
            jump += 1
        return jump

                