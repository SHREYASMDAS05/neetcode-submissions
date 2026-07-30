class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return string
            string += strs[0][i]
            
        return string