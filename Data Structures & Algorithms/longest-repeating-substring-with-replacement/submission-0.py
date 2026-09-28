class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init res, left pointer, and a count map {char:freq}
        res = 0 
        l = 0
        count = {}

        for r in range(len(s)):
            # grow window right and add s[r]
            count[s[r]] = count.get(s[r], 0) + 1

            # init most freq char in substring 
            max_freq = max(count.values())

            # check if window is invalid  
            # substring length - max_freq = number of chars you NEED to change
            # and if the num of chars you need to change is greater than k -> slide your window
            while ((r-l+1) - max_freq) > k:
                # remove s[l] from the count and also slide window 
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            
            # record the substring length 
            res = max(r-l+1, res)
        
        return res



    