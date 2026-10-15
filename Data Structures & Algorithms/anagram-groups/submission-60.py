class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # code : [associated words]
        for word in strs:
            code = [0]*26
            for c in word:
                code[ord(c) - ord('a')] += 1
            code = tuple(code)
            if code not in res:
                res[code] = []
            res[code].append(word)
        
        return list(res.values())