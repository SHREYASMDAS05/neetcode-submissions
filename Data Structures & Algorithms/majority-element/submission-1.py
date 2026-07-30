class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = nums[0]
        count = 0
        for i in nums:
            if count == 0:
                value = i
            if i == value:
                count+=1
            else:
                count-=1
        return value