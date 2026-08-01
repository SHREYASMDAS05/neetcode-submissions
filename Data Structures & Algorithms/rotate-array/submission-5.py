class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        m = len(nums)
        res = [0] * m
        k %= m
        for i in range(len(nums)):
            res[(i + k)% m] = nums[i]
        nums[:] = res
        return nums
        """
        n = len(nums) 
        def rotate(l , r):
            while l <=r:
                nums[l] , nums[r] = nums[r] , nums[l]
                l+=1
                r-=1
            return nums
        k = k%n
        rotate(0 , n-1)
        rotate( 0 , k-1)
        rotate(k , n-1)


