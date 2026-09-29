class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init a hashmap where the keys = char_code and values = [words with this char_code]
        res = {}

        # iter through input 
        for word in strs:
            # for each word determine it char code (26 elems long, value will represent occurences of char)
            code = [0] * 26
            for c in word:
                code[ord(c) - ord('a')] += 1
            # hashmap keys must be immutable 
            code = tuple(code)
            # init the res values if we haven't seen this code yet
            if code not in res:
                res[code] = []
            # append the associated anagrams to corresponding char_code (hashmap key)
            res[code].append(word)
        
        return list(res.values())


