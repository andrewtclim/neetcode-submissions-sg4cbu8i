class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Valid Substrs: len_substr - max_freq >= k 
        '''
        charMap = {} # {char : freq}
        res = 0 

        l = 0 
        for r in range(len(s)):
            # add r into hashmap and calc max freq
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            max_freq = max(charMap.values())

            # invalid case -> slide from left
            while (r-l+1) - max_freq > k:
                charMap[s[l]] -= 1
                l += 1
            # update valid substr length values 
            res = max(res, r-l+1)
        
        return res
            