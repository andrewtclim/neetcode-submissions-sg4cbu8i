class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        res = 0 

        # init sliding window pointers
        l = 0
        for r in range(len(s)):
            # add curr char into hashmap
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            # calc max freq
            max_freq = max(charMap.values())

            # invalid substrs -> slide window
            if (r-l+1) - max_freq > k:
                charMap[s[l]] -= 1 # decrement ( we know we've seen l before)
                l += 1
            
            # update res variable 
            res = max(res, (r-l+1))
        
        return res