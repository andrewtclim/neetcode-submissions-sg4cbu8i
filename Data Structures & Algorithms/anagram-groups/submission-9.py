# group anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize a hashmap (key = count_key and value = [associated words])
        res = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            # tuples are immutable and can be used as dict keys
            count_key = tuple(count)
            # initalize with empty lists (if it does not exist yet)
            if count_key not in res:
                res[count_key] = []
            # append associated word
            res[count_key].append(word)
        
        return list(res.values())


