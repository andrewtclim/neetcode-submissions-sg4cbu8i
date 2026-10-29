class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # first make sure that s1 could be a substr of s2
        if len(s1) > len(s2):
            return False
        
        # create char count codes for both substrs (i corresponds to letter)
        count_s1 = [0] * 26
        count_s2 = [0] * 26 

        # populate first window's code & compare
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        if count_s1 == count_s2:
            return True
        
        # slide window over the rest of s2, and compare with count_s1
        l = 0 
        for r in range(len(s1), len(s2)):
            # adds current char, subtracts leftmost char (slides by 1)
            count_s2[ord(s2[r]) - ord('a')] += 1
            count_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if count_s1 == count_s2:
                return True
        
        return False