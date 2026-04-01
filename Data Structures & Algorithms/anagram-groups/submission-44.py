class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap 
        res = {}

        # iterate over each word 
        for word in strs:
            # create char count tuple per word 
            char_count = [0] * 26 
            for c in word:
                char_count[ord(c) - ord("a")] += 1 
            # hashmap keys must be immutable
            char_count = tuple(char_count)

            # initalize charcount key with empty list 
            if char_count not in res:
                res[char_count] = []
            
            # populate hashmap with associated anagrams 
            res[char_count].append(word)
        
        return list(res.values())
                
