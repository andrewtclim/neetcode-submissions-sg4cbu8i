class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize sliding window pointer, return variable (longest length), hashset (keep unique chars)
        l, res = 0, 0 
        charSet = set()

        for r in range(len(s)):
            # duplicate case 
            while s[r] in charSet:
                # remove chars from the left until substring is unique 
                charSet.remove(s[l])
                l += 1
            # add unique chars
            charSet.add(s[r])
            # update substring length var
            res = max(res, r-l+1)
        
        return res
