class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashset to track chars in substr
        charSet = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            # check dupe -> slide left to keep cont.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res
