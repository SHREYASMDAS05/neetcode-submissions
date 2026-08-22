class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [(-cnt , char)  for char, cnt in count.items()]
        res =''
        time = 0 
        q = deque()
        while maxheap or q :
            time +=1
            

            if q and q[0][2] == time:
                cnt , char , readytime = q.popleft()
                
                heapq.heappush(maxheap , (cnt,char))
            if not maxheap:
                return ""
            cnt , char = heapq.heappop(maxheap)
            cnt +=1
            res += char
            if cnt != 0:
                q.append((cnt,char, time + 2))

        return res
