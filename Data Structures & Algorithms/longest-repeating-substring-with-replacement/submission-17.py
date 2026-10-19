class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        valid substrs: num_chars_replace <= k otherwise move up left pointer
        '''
        charMap = {}
        l = 0 
        res = 0

        for r in range(len(s)):
            # append to hashmap 
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            max_freq = max(charMap.values())

            # when valid update length var
            if (r-l+1) - max_freq <= k:
                res = max(res, r-l+1)
            else:
                charMap[s[l]] -= 1
                l += 1
            
        return res