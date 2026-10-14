class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Valid substr: substr_len - max_freq <= k 
        and if its invalid then move from l until it becomes valid 
        '''
        charSet = {}
        l, res = 0, 0

        for r in range(len(s)):
            # add current char to hashset 
            charSet[s[r]] = charSet.get(s[r], 0) + 1

            # calc max freq
            max_freq = max(charSet.values())

            # check validity 
            # invalid case where num_chars_replace > k
            if (r-l+1) - max_freq > k:
                # slide window form the left (contiguous)
                charSet[s[l]] -= 1
                l += 1
            else:
                res = max(res, r-l+1)
        
        return res