class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init res = Dict{char_code : List[associated_words]}
        res = {}

        for word in strs:
            # create char_code per word
            code = [0] * 26 
            for c in word: 
                code[ord(c)-96] += 1
            code = tuple(code)
            # init emply list for that code (first occurence)
            if code not in res:
                res[code] = []
            # then append the associated words with that code
            res[code].append(word)
        
        return list(res.values())