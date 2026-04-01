class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            sorted_key = tuple(sorted(word))
            if sorted_key not in res:
                res[sorted_key] = []
            res[sorted_key].append(word)
        
        return list(res.values())