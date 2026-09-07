class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                nei[pattern].append(word)

        visit = set()
        q = deque([beginWord])
        visit.add(beginWord)
        res = 1 
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neigword in nei[pattern]:
                        if neigword not in visit:
                            q.append(neigword)
                            visit.add(neigword)

            res +=1 

        return 0
