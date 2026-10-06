class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Valid substrs follow: (r-l+1) - max_freq <= k 
        If its invalid we must slide the window l -> r until it becomes valid
        Record valid substrs in a res variable
        '''
        res = 0 
        freq_map = {} # char : freq of char

        l = 0
        for r in range(len(s)):
            # add char to hashmap 
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            # calc max frequency in substr
            max_freq = max(freq_map.values())

            # invalid case: slide window and update corr hashmap 
            if (r-l+1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            # record substr length 
            res = max(res, (r-l+1))
        
        return res