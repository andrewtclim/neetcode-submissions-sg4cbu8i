class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init a hashset for subStr, var to store longest substr length 
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # found a dupe start deleting from the left
            while s[r] in charSet:
                # update hashset
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(r-l+1, res)
        
        return res
