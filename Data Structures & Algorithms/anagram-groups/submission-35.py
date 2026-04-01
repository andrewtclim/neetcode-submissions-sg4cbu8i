class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize a hashmap [char_count] -> [associated anagarams]
        res = {}

        for word in strs:
            # create char_count for each word
            char_count = [0] * 26 
            for c in word:
                char_count[ord(c)-ord('a')] += 1
            # tuples can be used as dict keys 
            char_count = tuple(char_count)

            # initalize hashmap with empty list values
            if char_count not in res:
                res[char_count] = []
            
            # append anagrams 
            res[char_count].append(word)
        
        # values in the res hashmap will be List[strs]
        return list(res.values())