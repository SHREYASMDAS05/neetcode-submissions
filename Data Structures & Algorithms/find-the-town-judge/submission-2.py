class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        score = [0] * (n+1)
        for u , v in trust:
            score[v] += 1
            score[u] -= 1 #if he trusts someone need to be penalty (he is not a judge)

        for person in range(1 , n+ 1):
            if score[person] == n-1:
                return person

        return -1
