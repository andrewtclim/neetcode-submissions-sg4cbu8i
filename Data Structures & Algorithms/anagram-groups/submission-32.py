class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap 
        res = {} # char_count -> [words with char count]

        for word in strs:
            # create char_count tuple for each word
            char_count = [0] * 26
            for c in word:
                char_count[ord(c) - ord('a')] += 1
            char_count = tuple(char_count)

            # initalize an empty list if char count not seen yet
            if char_count not in res:
                res[char_count] = []
            
            # append associated anagrams to that char count
            res[char_count].append(word)
        
        return list(res.values())
        