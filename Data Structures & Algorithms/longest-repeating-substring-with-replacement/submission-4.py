class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window approach (valid substrings and invalid substrings)
        Substrings are associated with a hashmap that counts the freq of chars (max freq)

        Valid -> just update the res value (longest valid substring length)
        Invalid -> slide the window from the left (decrement that char from the hashmap)

        NOTE: substrring length is calculated by r-l+1 so
        (r-l+1) - most_freq = num of chars that must be replaced to all be distinct 
        '''
        res = 0 
        l = 0
        count_map = {}

        # iter over chars in input string (r = current char pointer)
        for r in range(len(s)):
            # add this value to our count map
            count_map[s[r]] = count_map.get(s[r], 0) + 1
            # calculate the most frequent occuring char in the hashmap 
            most_freq = max(count_map.values())

            # check if this substr is valid (do we have enough chars to replace?)
            # invalid case 
            if (r-l+1) - most_freq > k:
                # update hashmap and slide the window from the left (keeps it contiguous) 
                count_map[s[l]] -= 1
                l += 1
            # valid case
            else:
                # record substr length
                res = max(res, r-l+1)
        
        return res