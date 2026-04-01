class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap (keys = char count tuple, values = [anagrams w/ char count])
        res = {}
        
        for word in strs:
            # create char count tuple for each word
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            count_key = tuple(count)
            if count_key not in res:
                res[count_key] = []
            # append associated anagrams with each count_key
            res[count_key].append(word)
        
        return list(res.values())
