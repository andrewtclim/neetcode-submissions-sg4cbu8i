class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init a hashmap {key=char_code and val=[words w/ char_code]}
        res = {}

        for word in strs:
            # build a char_code for each word
            char_code = [0] * 26
            for c in word:
                char_code[ord(c) - ord('a')] += 1
            # hashmap keys must be immutable
            char_code = tuple(char_code)
            if char_code not in res:
                res[char_code] = []
            # append to hashmap w/ char code
            res[char_code].append(word)
        
        return list(res.values())