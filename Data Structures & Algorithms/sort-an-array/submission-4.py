class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_arry(l , r):
            result = []
            i , j = 0 , 0 
            n , m = len(l) , len(r)
            while i < n and j < m:
                if l[i] < r[j]:
                    result.append(l[i])
                    i +=1
                else:
                    result.append(r[j])
                    j+=1

            if i < n:
                while i < n:
                    result.append(l[i])
                    i+=1
            if j < m:
                while j < m:
                    result.append(r[j])
                    j+=1

            return result

        if len(nums) <=1:
            return nums

        mid = len(nums)//2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        left = self.sortArray(left_arr)
        right = self.sortArray(right_arr)
        return merge_arry(left, right)

 
    


