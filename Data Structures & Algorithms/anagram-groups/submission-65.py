class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init a res hashmap {code : [associated anagrams]}
        res = {}

        for word in strs:
            # init a char code for each word
            code = [0] * 26 
            # encode this word's code
            for c in word:
                code[ord(c) - ord('a')] += 1
            # typecast as a tuple
            code = tuple(code)
            # init the start arr for this code if DNE
            if code not in res:
                res[code] = []
            res[code].append(word)
        
        return list(res.values())
