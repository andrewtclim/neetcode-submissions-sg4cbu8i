class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap
        res = {}

        for word in strs:
            # create char_key 
            char_key = [0] * 26 
            for c in word:
                char_key[ord(c)-ord('a')] += 1 
            char_key = tuple(char_key)
            if char_key not in res:
                res[char_key] = []
            res[char_key].append(word)
        
        return list(res.values())