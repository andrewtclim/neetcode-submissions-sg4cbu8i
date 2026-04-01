class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize res hashmap 
        res = {}

        for word in strs:
            count = [0] * 26 
            for c in word:
                count[ord(c) - ord('a')] += 1 
            count = tuple(count)
            if count not in res:
                res[count] = []
            res[count].append(word)
        
        return list(res.values())
        