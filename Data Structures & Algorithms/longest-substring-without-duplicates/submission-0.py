class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initalize hashset, two pointers, res variable (maximum substring length)
        charSet = set()
        l = 0
        res = 0

        # iterate through each char in string (r = current char)
        for r in range(len(s)):
            # duplicate char ->  remove duplicates starting from the left (substring must be contiguous)
            while s[r] in charSet: 
                charSet.remove(s[l])
                l += 1
            # unique char -> add this char to hashset
            charSet.add(s[r])
            # update result with the maximum length 
            # length = r-l+1 (since python has a 0-index)
            res = max(res, r-l+1)

        return res


