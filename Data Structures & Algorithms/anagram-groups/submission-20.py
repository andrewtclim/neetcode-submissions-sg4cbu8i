class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            # create char_count key for each word
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            count_key = tuple(count)
            # initalize an empty list for each count_key
            if count_key not in res:
                res[count_key] = []
            # append associated anagram to hashmap with count_key
            res[count_key].append(word)
        
        return list(res.values())
        