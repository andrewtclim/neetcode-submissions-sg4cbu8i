class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Valid substrs: len_substr - max_freq <= k 
        Invalid: len_substr - max_freq > k then we must slide left (contiguous)
        '''
        res = 0 
        charMap = {} # {char:freq}

        l = 0 
        for r in range(len(s)):
            # add current char into hashmap 
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            # max freq
            max_freq = max(charMap.values())

            # check validity 
            if (r-l+1) - max_freq > k:
                charMap[s[l]] -= 1
                l += 1
            else:
                res = max(res, r-l+1)
        
        return res