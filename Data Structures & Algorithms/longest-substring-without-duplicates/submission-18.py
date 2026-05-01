class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init hashset for longest substr 
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            # found duplicate -> slide left 
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            res = max(r-l+1, res)
            charSet.add(s[r])
        
        return res