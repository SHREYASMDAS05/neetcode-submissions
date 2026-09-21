class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            mp1[s[i]] = mp1.get(s[i],0) + 1
            mp1[t[i]] = mp1.get(t[i],0) - 1
            

        for count in mp1.values():
            if count != 0:
                return False
        return True  

        