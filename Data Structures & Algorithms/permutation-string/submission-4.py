class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Logic: Sliding window (contiguous)
        define char count arr for s1 and s2 
        let count_s2 be the current substring from s2 (same len as s1)
        slide window and check for its validity
        time complexity = O(26*n) -> O(n)
        '''
        
        # substring s1 must be smaller than s2
        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0]*26, [0]*26

        # populate char codes 
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        # check inital substring 
        if count_s1 == count_s2:
            return True 
        
        # NOTE: count_s1 stays constant and we compare curr substr to it

        # iter after the inital substr
        # init left pointer 
        l = 0 
        for r in range(len(s1), len(s2)):
            # add the r-th char  
            count_s2[ord(s2[r]) - ord('a')] += 1
            # remove the l-th char 
            count_s2[ord(s2[l]) - ord('a')] -= 1
            # slide window from left side 
            l += 1

            # check if substring is anagram
            if count_s1 == count_s2:
                return True
        
        # iter through all of s2... -> no substr anagram found
        return False



