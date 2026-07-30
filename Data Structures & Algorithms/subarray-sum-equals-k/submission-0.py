class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        res = 0
        prefixsum = {0:1}

        for i in nums:
            currsum += i
            diff = currsum - k
            if diff in prefixsum:
                res += prefixsum[diff]
            if currsum in prefixsum:
                prefixsum[currsum] += 1
            if currsum not in prefixsum:
                prefixsum[currsum] = 1

        return res

            
            
            