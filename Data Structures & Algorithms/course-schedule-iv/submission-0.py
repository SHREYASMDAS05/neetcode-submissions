class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq , crs in prerequisites:
            adj[crs].append(prereq)
        def dfs(crs):
            if crs not in prereqmap:
                prereqmap[crs] = set()
                for prereq in adj[crs]:
                    prereqmap[crs] = prereqmap[crs] | dfs(prereq)
                prereqmap[crs].add(crs)

            return prereqmap[crs]

        prereqmap = {}
        res = []
        for crs in range(numCourses):
            dfs(crs)
        for u , v in queries:
            res.append(u in prereqmap[v])

        return res
