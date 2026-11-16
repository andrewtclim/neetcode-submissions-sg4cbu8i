class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init var to store longest valid substr
        res = 0 
        # init hashmap to track substr's {char:freq}
        charMap = {}
        # init left pointer 
        l = 0 
        # logic rule: (substr_len-max_freq) = num chars needed to replace > k -> invalid
        # then u must move it (remove chars from left)

        # otherwise you should update your res variable 

        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            max_freq = max(charMap.values())

            if (r-l+1) - max_freq > k:
                charMap[s[l]] -= 1
                l += 1
            
            # update res with possible substr
            res = max(res, (r-l+1))
        
        return res