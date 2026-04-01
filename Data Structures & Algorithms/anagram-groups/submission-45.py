class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap {key=char_count, val=[list associated anagrams]}
        res = {}

        for word in strs:
            # create char count key for each word
            char_count = [0] * 26 
            for c in word:
                char_count[ord(c)- ord('a')] += 1
            char_count = tuple(char_count) # tuple immutable (so are strings, u could use sorted(word))

            # initalize char_count key with empty lists
            if char_count not in res:
                res[char_count] = []
            
            # append associated word with char_count
            res[char_count].append(word)
        
        return list(res.values())
