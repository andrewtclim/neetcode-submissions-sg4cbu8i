class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {char_count -> [anagrams w/ char_count]}
        res = {}

        for word in strs:
            # create char_count tuple for each word
            char_count = [0] * 26
            for c in word:
                char_count[ord(c)- ord('a')] += 1
            char_count = tuple(char_count)
            # initalize with empty arrays
            if char_count not in res:
                res[char_count] = []
            # populate each char_count
            res[char_count].append(word)
        
        return list(res.values())
            