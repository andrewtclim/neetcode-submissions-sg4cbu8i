class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding Window solution (window slides to find longest valid substr)
        Hashmap to count char freq in substring
        Max frequency variable (most freq char)
        Result variable (records longest valid substr)

        Logic:
        EX) "AABAAB" needs to change 2 letters to be valid, the most freq char is A (4 letters)
        Length of Substring - Most Frequent Letter = Num of letters required to change 
        6 - 4 = 2 

        When its valid -> record substring length
        When it's invalid -> slide the window, update hashmap until it is valid
        '''
        count = {}
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            # record char freq in hashmap 
            count[s[r]] = count.get(s[r], 0) + 1
            # calc the most freq char in substr
            max_freq = max(max_freq, count[s[r]])

            # invalid substr -> slide left until it becomes valid
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # always record the substring length 
            res = max(res, r - l + 1)

        return res



    