class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap [char_count] -> [anagrams w/ char count]
        res = {}

        for word in strs:
            # create a char count tuple for each word 
            char_count = [0] * 26
            for c in word:
                char_count[ord(c)-ord('a')] += 1
            char_count = tuple(char_count)

            # initalize hashmap with empty lists
            if char_count not in res: 
                res[char_count] = []
            
            # append associated anagrams to char_count
            res[char_count].append(word)
        
        return list(res.values())
        