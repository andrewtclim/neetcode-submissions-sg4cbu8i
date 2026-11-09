class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # init char codes for both substrs
        # s2 will be the dynamic substr code that we compare with s1 later
        counts1, counts2 = [0]*26, [0]*26 

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        
        # if the first window matches -> permutation found
        if counts1 == counts2:
            return True

        # sliding window to check the other potential substrs
        l = 0
        for r in range(len(s1), len(s2)):
            # add curr char and remove the left char
            counts2[ord(s2[r]) - ord('a')] += 1
            counts2[ord(s2[l]) - ord('a')] -= 1
            l += 1
        
            if counts1 == counts2:
                return True
        
        return False
