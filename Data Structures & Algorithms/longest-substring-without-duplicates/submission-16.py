class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init sliding window (left), max length variable, and hashset for current substring
        l, res = 0, 0 
        charSet = set()

        for r in range(len(s)):
            # check for uniqueness (if dupe -> remove from left side)
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # update max length
            res = max(res, r-l+1)
            charSet.add(s[r])

        return res 
        