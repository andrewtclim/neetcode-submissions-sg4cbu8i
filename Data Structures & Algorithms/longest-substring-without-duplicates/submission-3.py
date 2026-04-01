class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize sliding window pointers (left, right (current) will be in loop)
        # initalize return var (longest substring), hashset (unique chars in substring)
        l = 0 
        res = 0 
        charSet = set()

        for r in range(len(s)):
            # duplicate found -> slide left pointer until substring is unique/no repeats
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # unique char found -> add to hashset, update res
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res
