class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize a hashmap {char_count -> [anagrams w/ char_count]}
        res = {}

        for word in strs:
            # create char_count per word
            char_count = [0] * 26 
            for c in word:
                char_count[ord(c)- ord("a")] += 1
            # must be a tuple (tuples are hashable/immutable objects)
            char_count = tuple(char_count)

            # initalize hashmap with empty arr (new char_count seen)
            if char_count not in res:
                res[char_count] = []
            
            # populate hashmap with associated anagrams
            res[char_count].append(word)
        
        return list(res.values())
        