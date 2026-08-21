class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = []
        for i in nums:
            heapq.heappush(ans , i)
            if len(ans) >  k:
                heapq.heappop(ans)

        return ans[0]
