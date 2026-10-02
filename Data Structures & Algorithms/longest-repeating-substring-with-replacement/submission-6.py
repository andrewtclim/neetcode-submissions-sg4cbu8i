class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Logic: 
        substr_len = r-l+1
        substr_len - max_freq = number of elems needed to change
        if (substr_len - max_freq) > k -> then its invalid and we must slide
        '''

        freq_map = {}
        res = 0
        l = 0 

        # r is the current pointer
        for r in range(len(s)):
            # add r into the substr (update its hashmap), calc max freq
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(freq_map.values())

            # invalid case (not enough k-chars)
            while (r-l+1 - max_freq) > k:
                freq_map[s[l]] -= 1
                l += 1
            
            # valid cases 
            res = max(r-l+1, res)

        return res
