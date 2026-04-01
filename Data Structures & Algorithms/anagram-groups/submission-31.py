class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap char_count -> [words, ...]
        res = {}

        for word in strs:
            # create a char_count key for each word
            char_count = [0] * 26 
            for c in word:
                char_count[ord(c) - ord("a")] += 1
            char_count = tuple(char_count)

            if char_count not in res:
                res[char_count] = []

            res[char_count].append(word)

        return list(res.values())        