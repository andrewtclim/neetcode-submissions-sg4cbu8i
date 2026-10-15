class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        LOGIC:
        valid substr: (r-l+1)-max_freq <= k
        invalid: (r-l+1)-max_freq > k -> need to slide left 
        '''
        res = 0 
        charFreq = {} # {char : freq}

        l = 0 
        for r in range(len(s)):
            # add current char to hashmap 
            charFreq[s[r]] = charFreq.get(s[r], 0) + 1

            # calc max freq
            max_freq = max(charFreq.values())

            # check validity -> slide until it is valid
            if (r-l+1) - max_freq > k:
                charFreq[s[l]] -= 1
                l += 1
            
            # record
            res = max(res, r-l+1)
        
        return res