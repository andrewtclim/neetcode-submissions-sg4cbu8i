class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize left pointer and res
        l, res = 0, 0
        charSet = set()

        # right pointer of window 
        for r in range(len(s)):
            # if we find a duplicate, slide l window until no dupes round
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # unique char found 
            charSet.add(s[r])
            # update res 
            res = max(res, r-l+1)
        return res