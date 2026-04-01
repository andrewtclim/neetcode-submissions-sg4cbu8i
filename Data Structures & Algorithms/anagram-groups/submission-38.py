class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap {sorted_word -> [associated anagrams]}
        res = {}

        for word in strs:
            # use the sorted word as a key
            # sorted returns a list of strings, convert to a hashable object (tuple)
            sorted_word = tuple(sorted(word))

            if sorted_word not in res:
                res[sorted_word] = []
            
            res[sorted_word].append(word)
        
        return list(res.values())