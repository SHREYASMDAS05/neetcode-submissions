class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums) -1):
            res[i+1] = prefix * nums[i]
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -2 , -1,-1):
            res[i] *= postfix * nums[i+1]
            postfix *= nums[i+1]
        return res

            