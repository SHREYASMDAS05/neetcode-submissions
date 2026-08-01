class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i = 0
        j = 0
        res = 0
        while i < len(s):
            if s[i] in mp and mp[s[i]] >= j:
                j = mp[s[i]] + 1
                
            mp[s[i]] = i
            res = max(i -j + 1 , res)
            i+=1
            

                
                
                

        return res
                

