class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in mp:
                mp[sorted_word].append(word)
            else:
                mp[sorted_word] = [word]
        return list(mp.values())