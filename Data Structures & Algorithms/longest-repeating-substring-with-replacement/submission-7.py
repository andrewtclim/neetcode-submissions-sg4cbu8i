class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window to stay contiguous and substrings
        Logic: (r-l+1) - max_freq = num of chars needed to replace 
        if (r-l+1) - max_freq > k -> then we must slide window from left
        otherwise record the valid substring length 
        '''

        l, res = 0, 0
        freq_map = {}

        # r is our current pointer 
        for r in range(len(s)):
            # add to freq_map
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            # calc max frequent 
            max_freq = max(freq_map.values())

            # check valid 
            # invalid case 
            if (r-l+1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            else:
                res = max(res, r-l+1)
        
        return res