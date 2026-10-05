class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Valid substrs are those that pass condition
        (r-l+1) - max_freq <= k (we have enough chars to replace)
        Init a hashmap to track chars and freq in substr
        Init left pointer and res variable records max substr length
        '''
        freq_map = {}
        l, res = 0, 0 

        for r in range(len(s)):
            # add s[r] to our freq_map 
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            # calc max freq
            max_freq = max(freq_map.values())

            # check validity 
            # invalid case (slides to l)
            if ((r-l+1) - max_freq) > k:
                freq_map[s[l]] -= 1
                l += 1
            # valid cases -> record substr length 
            else:
                res = max(res, r-l+1)
        
        return res
