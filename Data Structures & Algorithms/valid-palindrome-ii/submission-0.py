class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(l , r):
            while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False

            return True

        l , r = 0 , len(s) -1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return (ispalindrome(l+1 ,r) or ispalindrome(l , r-1))

        return True
        
            
