class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curSet = set()
        res = 0

        # pointer for start of continuous substring
        l = 0
        for r in range(len(s)):
            # check unqiueness -> 
            # keep removing from left until unique 
            while s[r] in curSet:
                curSet.remove(s[l])
                l += 1
            # add the next char to hashset 
            curSet.add(s[r])
            # update res value 
            res = max(res, r-l+1)
        
        return res
