class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i , curr , total):
            if total == target:
                res.append(curr.copy())
                return
            for j in range(i , len(candidates)):
                if total + candidates[j] > target:
                    return 
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                dfs(j+1 , curr , total + candidates[j])
                curr.pop()

        dfs(0 , [] , 0)
        return res

            