class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_big = -heapq.heappop(heap)
            second_big = -heapq.heappop(heap)

            if first_big == second_big:
                continue
            if first_big != second_big:
                new = -abs(first_big - second_big)

            heapq.heappush(heap , new)

        return -heap[0] if heap else 0
