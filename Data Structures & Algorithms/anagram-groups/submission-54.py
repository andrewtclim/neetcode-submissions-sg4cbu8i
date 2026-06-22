class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init hashmap {char_code : [anagrams of code]}
        res = {}

        for word in strs:
            char_code = [0] * 26 
            for c in word:
                char_code[ord(c) - ord('a')] += 1
            char_code = tuple(char_code)
            if char_code not in res:
                res[char_code] = []
            res[char_code].append(word)
        
        return list(res.values())