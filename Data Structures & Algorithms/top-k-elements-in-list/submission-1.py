class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        mp = {}
        for i in nums:
            if i in mp:
                mp[i] +=1
            else:
                mp[i] = 1
        result = []
        sorted_list = sorted(mp.items() , key = lambda  item : item[1] , reverse = True)
        for key , val in sorted_list:
            if len(result) == k:
                return result
            result.append(key)
        return result
        '''
        mp = {}
        for i in nums:
            mp[i] = mp.get(i ,0) + 1
        bucket = [[] for i in range(len(nums) + 1)]
        for num , freq in mp.items():
            bucket[freq].append(num)
        res = []
        for freq in range(len(bucket) - 1 , 0 , -1):
            for num in bucket[freq]:
                res.append(num)

                if len(res) == k:
                    return res