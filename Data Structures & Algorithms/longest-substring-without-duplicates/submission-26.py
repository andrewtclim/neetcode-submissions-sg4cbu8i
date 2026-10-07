class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init a hashset and pointers
        charSet = set()
        l = 0
        charLength = 0

        # iter over string (r = current char index)
        for r in range(len(s)):
            # duplicate case (slide from left)
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # add current char
            charSet.add(s[r])

            # unqiue case (record)
            charLength = max(r-l+1, charLength)
        
        return charLength

