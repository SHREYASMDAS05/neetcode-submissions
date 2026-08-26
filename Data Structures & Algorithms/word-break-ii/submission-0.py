class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        worddict = set(wordDict)
        curr = []
        res = []
        def backtrack(i):
            if i == len(s):
                res.append(' '.join(curr))
            for j in range(i , len(s)):
                w = s[i:j+1]
                if w in worddict:
                    curr.append(w)
                    backtrack(j+1)
                    curr.pop()

        backtrack(0)
        return res