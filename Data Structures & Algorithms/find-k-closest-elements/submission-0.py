class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0 , len(arr) - k

        while l < r :
            m = (l + r)//2
            if abs(x - arr[m]) > abs(arr[m + k] - x):
                l = m + 1
            else:
                r = m
        return arr[l:l+k]

