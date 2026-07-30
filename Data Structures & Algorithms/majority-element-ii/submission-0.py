class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] +=1 
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n , c in count.items():
                new_count[n] = c-1
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums)//3:
                res.append(n)

        return res