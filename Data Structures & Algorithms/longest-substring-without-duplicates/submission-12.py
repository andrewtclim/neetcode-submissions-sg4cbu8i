class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init left pointer of window and var to store substring length 
        # hashset for substrings unique letters
        l, res = 0, 0 
        charSet = set()

        # iter over chars
        for r in range(len(s)):
            # if find dupe start sliding window left until unique
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # otherwise keep moving and add to substring
            charSet.add(s[r])
            # update length 
            res = max(res, r-l+1)
        
        return res

