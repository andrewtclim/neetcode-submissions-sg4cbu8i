class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window and a hashmap (contiguous substr and char frequency)

        Logic: valid substrings are those that meet: num_chars_req_swap <= k
        where num_chars_req = substr_len - max_freq 

        if it doesnt meet that condition (invalid):
            then we should slide the window and delete the char from the left
        '''
        charMap = {}
        l = 0
        res = 0 

        for r in range(len(s)):
            # add char into hashmap 
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            max_freq = max(charMap.values())
            
            # check validity 
            # invalid -> slide from left
            if (r-l+1) - max_freq > k:
                charMap[s[l]] -= 1
                l += 1
            # otherwise record the substring length 
            res = max(res, r-l+1)

        return res
