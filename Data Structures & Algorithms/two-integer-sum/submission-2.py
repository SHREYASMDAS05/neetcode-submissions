class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        
        mp = {}
        for i in range(len(nums)):
            if target - nums[i] in mp:
                return [mp[target-nums[i]] , i]
            else:
                mp[nums[i]] = i
                