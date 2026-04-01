class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize left pointer (sliding window), res variable, hashset
        l = 0
        res = 0 
        charSet = set()

        # iterate with right pointer 0 -> last index
        for r in range(len(s)):
            # duplicate char found in hashset
            while s[r] in charSet:
                # slide from the left until substring is uniquq
                charSet.remove(s[l])
                l += 1
            # unqiue char found
            charSet.add(s[r])
            res = max(res, r-l+1) 

        return res