class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        passchange = [0] * 1001

        for t in trips:
            numpass , start , end = t
            passchange[start] += numpass
            passchange[end] -= numpass
        currpass = 0
        for i in range(1001):
            currpass += passchange[i]
            if currpass > capacity:
                return False

        return True'''

        trips.sort(key = lambda t:t[1])
        maxheap =[] #pairs of end , numpass
        currpass = 0
        for t in trips:
            numpass , start , end = t
            while maxheap and maxheap[0][0] <= start:
                currpass -= maxheap[0][1]
                heapq.heappop(maxheap)

            currpass += numpass
            if currpass > capacity:
                return False
            heapq.heappush(maxheap , ( end , numpass))

        return True


