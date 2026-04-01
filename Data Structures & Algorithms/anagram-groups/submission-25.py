class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap (keys = char count and values = associated anagrams)
        res = {}
        # create a count key for each word 
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            count_key = tuple(count)
            if count_key not in res:
                res[count_key] = []
            res[count_key].append(word)
        
        return list(res.values())
        