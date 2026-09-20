class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        maxi = nums[0]
        for i in range(1 , n):
            curr = max(nums[i] , curr + nums[i])
            maxi = max(curr , maxi)
        return maxi
        

