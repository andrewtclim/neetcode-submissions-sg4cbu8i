class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init hashset to track unique substring 
        # res variable for the max substrings length
        # left pointer for the start of the substring 
        charSet = set()
        res = 0
        l = 0 

        # l and r pointers: l and r define the substring = s[l:r]
        for r in range(len(s)):
            while s[r] in charSet:
                # delete from the left -> substring
                charSet.remove(s[l])
                l += 1
            # new char found 
            charSet.add(s[r])
            res = max(res, r-l+1)
    
        return res