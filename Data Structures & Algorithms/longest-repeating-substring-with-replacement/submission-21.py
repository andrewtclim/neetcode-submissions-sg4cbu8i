class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hashmap to keep track of substrs {char : freq}
        charMap = {}
        res = 0 # variable for longest valid substrs

        l = 0 
        for r in range(len(s)):
            # add this char to the hashmap 
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            # calc max freq 
            max_freq = max(charMap.values())

            # valid substrs: those where the num of chars to replace >= k
            if (r-l+1) - max_freq > k:
                charMap[s[l]] -= 1 # decrement this char 
                l += 1

            # valid substrs -> update res
            res = max(res, r-l+1)

        return res