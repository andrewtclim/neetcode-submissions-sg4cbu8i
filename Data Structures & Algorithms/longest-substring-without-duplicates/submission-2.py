class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize pointers for sliding window, result variable, hashset
        l = 0 
        res = 0
        charSet = set()

        # r = current pointer (rightside of sliding window)
        for r in range(len(s)):

            # repeated char found -> shrink window until our substring is unique
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # new char found -> add to hashset, update res (length of substring)
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res
