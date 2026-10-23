class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        res = 0 

        for r in range(len(s)):
            # check for duplicate -> slide window
            while s[r] in charSet:
                # slide left -> right
                charSet.remove(s[l])
                l += 1

            # add current char to hashset
            charSet.add(s[r])
            
            # substr is valid -> update res
            res = max(res, r-l+1)
        
        return res

