class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        charMap = {} # char : freq
        res = 0 

        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            max_freq = max(charMap.values())

            while (r-l+1) - max_freq > k:
                # slide window from left -> until valid substr
                charMap[s[l]] -= 1
                l += 1
            
            # valid substrs get updated to res 
            res = max(res, r-l+1)
        
        return res