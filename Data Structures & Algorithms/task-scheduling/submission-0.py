class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q = deque() #pairs in [cnt , time + n ]
        time = 0
        while q or maxheap:
            time +=1 
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt!= 0:
                    q.append((cnt , time + n))
            if q and q[0][1] == time:
                back = q.popleft()[0]
                heapq.heappush(maxheap , back)


        return time

            