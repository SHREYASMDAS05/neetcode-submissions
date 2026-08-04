class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        l , r = 0 , len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m 
            if nums[m] > target :
                r = m-1
            else:
                l = m + 1
            
            

        return l

            