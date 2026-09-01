class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for course , prereq in prerequisites:
            indegree[course] +=1
            graph[prereq].append(course)

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        cnt = 0
        while q:
            course = q.popleft()
            cnt +=1
            for next_course in graph[course]:
                indegree[next_course] -=1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return cnt == numCourses


'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        state = [0] * numCourses

        def dfs(course):
            # Cycle found
            if state[course] == 1:
                return False

            # Already completely processed
            if state[course] == 2:
                return True

            # Currently visiting
            state[course] = 1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            # Finished processing this course
            state[course] = 2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        '''

