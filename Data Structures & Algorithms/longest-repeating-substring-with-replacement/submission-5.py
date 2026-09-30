class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init hashmap to track substrs char and freq
        # num_chars_replaced = substr_length - max_frequent_char 
        # valid when num_chars_replaced <= k 
        count = {}
        res = 0
        l = 0

        # r = current char pointer
        for r in range(len(s)):
            # update and add s[r] into the hashmap
            count[s[r]] = count.get(s[r], 0) + 1
            # find the most frequent char value from hashmap 
            most_freq = max(count.values())

            # check substr validity 
            # invalid case (not enough k chars to replace)
            # slide window from left (contiguous)
            while ((r-l+1) - most_freq) > k:
                count[s[l]] -= 1
                l += 1
            
            # valid case -> record new substr length 
            res = max(res, r-l+1)

        return res