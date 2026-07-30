class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0
        for i in st:
            if i -1 not in st:
                length = 0 
                while i + length in st:
                    length +=1

                longest = max(longest , length)

        return longest

         