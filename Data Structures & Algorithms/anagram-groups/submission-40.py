class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap {char_count -> [associated anagrams]}
        res = {}

        for word in strs:
            # create char_count tuple for each word
            char_count = [0] * 26
            for char in word:
                char_count[ord(char)-ord('a')] += 1
            char_count = tuple(char_count)

            # initalize hashmap values with [] (if char_count has not been seen yet)
            if char_count not in res:
                res[char_count] = []
            
            # populate hashmap with associated anagrams 
            res[char_count].append(word)
        
        # return the values of the hashmap as a list of lists 
        return list(res.values())