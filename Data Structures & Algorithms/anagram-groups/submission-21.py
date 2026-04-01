class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap (key = character count_key, values = [anagrams with the same count_key])
        res = {}

        for word in strs:
            # create count key and initalize with empty lists
            count = [0] * 26 
            for c in word:
                count[ord(c) - ord('a')] += 1 
            count_key = tuple(count)
            if count_key not in res:
                res[count_key] = []
            
            # append associated words with count_key
            res[count_key].append(word)
        
        return list(res.values())
        