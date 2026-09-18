class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window to track the length of our substrings dynamically
        # hashset to ensure that the substring is unique 
        charSet = set() 
        # res is our max length and l is the left pointer in sliding window
        res, l = 0, 0 

        # iter over index in string (right pointer)
        for r in range(len(s)):
            # check if this char is in the hashset 
            # start sliding the window from the left until substr is unique
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # if its not then add it to the hashset and update our res variable 
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res

