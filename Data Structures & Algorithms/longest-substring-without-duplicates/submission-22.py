class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init hashset for unique chars, left pointer and res (substring length)
        charSet = set()
        res, l = 0, 0 

        for r in range(len(s)):
            # check unqiueness start removing from left
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # add new unique char to set 
            charSet.add(s[r])
            # calc substring length and update 
            res = max(res, r-l+1)
        
        return res
