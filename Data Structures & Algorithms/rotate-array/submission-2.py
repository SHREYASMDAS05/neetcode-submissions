class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        res = [0] * m
        k %= m
        for i in range(len(nums)):
            res[(i + k)% m] = nums[i]
        nums[:] = res
        return nums