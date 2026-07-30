class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3>0:
                    k-=1
                elif sum3<0:
                    j+=1
                else:
                    output.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and  nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
        
        return output

        