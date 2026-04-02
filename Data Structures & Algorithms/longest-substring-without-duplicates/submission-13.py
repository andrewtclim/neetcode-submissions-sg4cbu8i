class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init a hashset for unique substring, left pointer and length variable 
        l, res = 0, 0 
        charSet = set()

        for r in range(len(s)):
            # slide left pointer until substr is unique 
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # otherwise add chars to the substr 
            charSet.add(s[r])
            # calculate the substrs length and update 
            res = max(res, r-l+1)
        
        return res