class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        We use a combo of sliding window and char_code array 
        - slide window to keep contiguous
        - char_code arr to check anagram validity (O(26n) -> O(n))

        First check that s1 can be a substr of s2
        Then check the first substr window 
        Then iteratively slide across s2 and check validity 
        '''

        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0]*26, [0]*26

        # populate char codes (first substr window)
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        if count_s1 == count_s2:
            return True

        # init l pointer 
        l = 0
        # check the other window 
        for r in range(len(s1), len(s2)):
            # slide window of count_s2 (right)
            count_s2[ord(s2[r]) - ord('a')] += 1
            # remove the leftmost char 
            count_s2[ord(s2[l]) - ord('a')] -= 1
            # update l pointer
            l += 1
            # check anagram match 
            if count_s1 == count_s2:
                return True
        
        # otherwise no matches found...
        return False


