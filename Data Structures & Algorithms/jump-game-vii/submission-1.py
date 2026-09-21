class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q , farthest = deque([0]) , 0
        if s[-1] == '1':
            return False
        while q:
            idx = q.popleft()
            start = max(farthest , idx + minJump)
            for j in range(start , min(idx + maxJump + 1 , len(s))):
                if s[j] == '0':
                    q.append(j)
                if j == len(s) -1:
                    return True
                
            farthest = max(farthest , idx + maxJump)
        return False
        