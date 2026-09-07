class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for word in words:
            for c in word:
                adj[c]
        for i in range(len(words)-1):
            w1 , w2 = words[i] , words[i+1]
            minlen = min(len(w1) , len(w2))
            if len(w1)> len(w2)  and w1[:minlen] == w2[:minlen]:
                return ''
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        res = []
        visit = {} # False for visited True for in the path
        def dfs(c):
            if c in visit:
                return visit[c] # True if cycle detected (got the char which is still in processing)

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return '' 
        res.reverse()
        return ''.join(res)