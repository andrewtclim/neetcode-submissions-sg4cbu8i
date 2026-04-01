class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize left pointer, res var, and hashset 
        l, res = 0, 0 
        charSet = set()

        for r in range(len(s)):
            # duplicate char found 
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # unique char found (add to hashset, update substring length)
            charSet.add(s[r])
            res = max(res, r-l+1)

        return res