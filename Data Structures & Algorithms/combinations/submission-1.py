'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(n):
            arr.append(i+1)
        res = []
        def dfs(i , curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i >= len(arr):
                return
            curr.append(arr[i])
            dfs(i+1 , curr)
            curr.pop()
            dfs(i+1 , curr)
        dfs(0 ,[])

        return res
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            for j in range(i, n + 1):
                curr.append(j)
                dfs(j + 1, curr)
                curr.pop()

        dfs(1, [])
        return res
