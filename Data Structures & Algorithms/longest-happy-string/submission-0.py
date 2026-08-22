class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []

        if a > 0:
            heapq.heappush(maxheap, (-a, 'a'))
        if b > 0:
            heapq.heappush(maxheap, (-b, 'b'))
        if c > 0:
            heapq.heappush(maxheap, (-c, 'c'))
        res = ''
        while maxheap:
            cnt , char =heapq.heappop(maxheap)

            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxheap:
                    break

                cnt2 , char2 = heapq.heappop(maxheap)
                res+=char2
                cnt2+=1
                if cnt2 != 0:
                    heapq.heappush(maxheap , (cnt2 , char2))

                heapq.heappush(maxheap,(cnt,char))

            else:
                res += char
                cnt +=1
                if cnt != 0:
                    heapq.heappush(maxheap,(cnt,char))

        return res