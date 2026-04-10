class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init hashmap {tuple(char_code) : [associated words]}
        res = {}

        for word in strs:
            # create a char code for each word 
            char_code = [0] * 26
            for char in word:
                char_code[ord('a') - ord(char)] += 1
            char_code = tuple(char_code)
            # init char code in hashmap (if it DNE yet)
            if char_code not in res:
                res[char_code] = []
            # append associated word into hashmap 
            res[char_code].append(word)
        
        return list(res.values())