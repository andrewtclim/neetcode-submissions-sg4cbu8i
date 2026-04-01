class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize sliding window pointer, res variable, and hashset (unique chars in substring)
        l = 0 
        res = 0
        charSet = set()

        for r in range(len(s)):
            # found repeated char
            while s[r] in charSet:
                # remove letter from left of substring 
                # shift substring one left 
                charSet.remove(s[l])
                l += 1
            # unique char found 
            charSet.add(s[r])
            # update res
            res = max(res, r-l+1)
        
        return res
