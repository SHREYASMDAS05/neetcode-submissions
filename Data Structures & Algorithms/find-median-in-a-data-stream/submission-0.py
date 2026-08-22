class MedianFinder:

    def __init__(self):
        self.small , self.large = [] , []
        #small max_heap and large = min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small ,-1 * num)
        #check if all the element in smll is less than large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large , val)

        #check if the length are equal
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large , val)
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small , val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            num1 = self.small[0]
            num2 = self.large[0]
            return (-num1 + num2) /2
        
        
        