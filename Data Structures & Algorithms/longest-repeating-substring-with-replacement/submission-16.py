class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        valid substrs: num_chars_replace <= k otherwise move up left pointer
        '''
        charMap = {}
        l = 0 
        longestStr = 0

        for r in range(len(s)):
            # append to hashmap 
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            max_freq = max(charMap.values())

            if (r-l+1) - max_freq > k:
                charMap[s[l]] -= 1
                l += 1
            else:
                longestStr = max(longestStr, r-l+1)
            
        return longestStr