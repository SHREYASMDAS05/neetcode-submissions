class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = {}
        mp2 = {}
        for i in s1:
            if i in mp1:
                mp1[i] +=1
            else:
                mp1[i] = 1
        
        l , r = 0 , 0 
        while r < len(s2):
            
            if r - l +1 > len(s1):
                mp2[s2[l]] -=1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l+=1

            if s2[r] in mp2:
                mp2[s2[r]] += 1
            else:
                mp2[s2[r]] = 1
            r+=1
            if mp1 == mp2:
                return True

        return False
