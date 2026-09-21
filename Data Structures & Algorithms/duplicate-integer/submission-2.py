class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in nums:
            if i in mp:
                return True
            else:
                mp[i] = 1
        
        return False

        