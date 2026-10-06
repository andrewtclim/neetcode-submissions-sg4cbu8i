class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        lets group the anagrams together by their char_code 
        for this we will use a hashmap {char_code : [associated words]}
        '''

        res = {}

        for word in strs:
            char_code = [0]*26
            for c in word:
                char_code[ord(c) - ord('a')] += 1
            char_code = tuple(char_code)
            if char_code not in res:
                res[char_code] = []
            # append associated word
            res[char_code].append(word)
        
        return list(res.values())