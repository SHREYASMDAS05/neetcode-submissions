
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans =[]
        for x ,(i , j) in enumerate(points):
            dist = i**2 + j**2
            ans.append([dist , i, j])
        res = []
        heapq.heapify(ans)
        while k > 0:
            dist , x , y = heapq.heappop(ans)
            res.append([x, y])
            k-=1

        return res

            