class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums)//2
        nums= sorted(nums)
        return nums[mid]
