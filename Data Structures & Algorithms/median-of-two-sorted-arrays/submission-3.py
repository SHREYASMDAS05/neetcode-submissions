class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2
        total = len(A) + len(B)
        half = total //2 
        if len(A) > len(B):
            A , B = B , A

        l , r = 0 , len(A) -1
        while True:
            mA = (l + r) // 2
            mB = half - mA -2

            Aleft = A[mA] if mA >= 0 else float('-inf')
            Aright  = A[mA + 1] if mA + 1 <len(A) else float('inf')
            Bleft = B[mB] if mB >= 0 else float('-inf')
            Bright = B[mB + 1] if mB + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                #if odd
                if total % 2:
                    return min(Aright , Bright)

                else:
                    return (max(Aleft , Bleft) + min(Aright , Bright)) / 2

            elif Aleft >Bright:
                r = mA - 1
            else:
                l = mA + 1
        
        