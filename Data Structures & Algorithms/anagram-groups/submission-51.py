class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init a hashmap {char_code : [associated words]}
        res = {}

        for word in strs:
            char_code = [0] * 26 
            for c in word:
                char_code[ord(c) - ord('a')] += 1
            # hashmap keys must be immutable
            char_code = tuple(char_code)

            # initalize empty list for that char_code 
            if char_code not in res:
                res[char_code] = []
            
            # append associated words into that char_code list 
            res[char_code].append(word)
        
        return list(res.values())
            