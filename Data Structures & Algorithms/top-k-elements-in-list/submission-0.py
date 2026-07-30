class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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