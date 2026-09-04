class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first init a hashmap 
        # {char_code tuple : [associated words]}
        res = {}

        # iter over words
        for word in strs:
            # create a char code for that word
            code = [0] * 26 
            for c in word:
                code[ord(c) - ord('a')] += 1
            # type cast as immutable tuple 
            code = tuple(code)
            # init char code in hashmap 
            if code not in res:
                res[code] = []
            # append associated word into value list 
            res[code].append(word)
        
        return list(res.values())