class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap {char_count -> [associated anagrams]}
        res = {}

        for word in strs:
            # create a char count key per word
            char_count = [0] * 26 
            for c in word:
                char_count[ord(c)-ord('a')] += 1
            char_count = tuple(char_count)

            # initalize hashmap with empty list 
            if char_count not in res:
                res[char_count] = []
            
            # populate hashmap with associated anagrams
            res[char_count].append(word)
        
        return list(res.values())