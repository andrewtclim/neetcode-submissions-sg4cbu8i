class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init hashset of substring, init l pointer
        charset = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            res = max(r-l+1, res)
            charset.add(s[r])

        return res
            
