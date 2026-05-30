class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # {char_code tuple : [associated words]}

        for word in strs:
            # each word gets its own tuple 
            char_code = [0] * 26
            for c in word:
                char_code[ord(c) - ord('a')] += 1
            char_code = tuple(char_code)
            if char_code not in res:
                res[char_code] = []
            res[char_code].append(word)
        
        return list(res.values())