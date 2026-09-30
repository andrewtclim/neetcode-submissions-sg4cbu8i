class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init hashset to track substrings unique chars
        hashset = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            # duplicate case found in hashset -> start sliding window from left (contiguous string)
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1 
            # otherwise add char to hashset and also record substring length 
            hashset.add(s[r])
            res = max(res, r-l+1)
        
        return res