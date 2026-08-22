class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
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

        return True
