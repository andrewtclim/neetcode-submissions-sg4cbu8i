class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init hashmap for result 
        res = {}

        for word in strs:
            # create unique char code foe every word 
            code = [0] * 26 
            for c in word:
                code[ord(c) - ord('a')] += 1
            # hashmap keys must be immutable 
            code = tuple(code)
            # init hashmap key if it dne in the hashmap 
            if code not in res:
                res[code] = []
            # append associated word into the hashmap 
            res[code].append(word)
        
        return list(res.values())
        