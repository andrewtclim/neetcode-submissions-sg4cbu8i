class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init hashmap {char_code : [words with same char_count]}
        res = {}

        for word in strs:
            # init a char_code for each word 
            code = [0] * 26 
            for c in word:
                code[ord(c) - ord('a')] += 1
            # hashmap keys must be immutable 
            code = tuple(code)
            # init code in hashmap if DNE 
            if code not in res:
                res[code] = []
            # attach associated words
            res[code].append(word)
        
        return list(res.values())