class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize res var (stores max length of substring)
        # initalize hashset (ensures substring is unique)
        # left pointer for the left (start of our substring)
        res = 0 
        charSet = set()
        l = 0

        for r in range(len(s)):
            # duplicate case
            while s[r] in charSet:
                # delete chars from the left of substring 
                charSet.remove(s[l])
                l += 1
            # unique char found 
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res
        