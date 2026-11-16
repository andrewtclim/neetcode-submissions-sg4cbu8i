class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # init char codes for both substrs
        codes1 = [0]*26
        codes2 = [0]*26

        # s1 must be smaller than s2, if s2 were to contain a permu. of s1
        if len(s1) > len(s2):
            return False

        # populate the first substring window 
        for i in range(len(s1)):
            codes1[ord(s1[i]) - ord('a')] += 1
            codes2[ord(s2[i]) - ord('a')] += 1

        # compare the two
        if codes1 == codes2:
            return True

        # shift windows of s2, compare 
        l = 0 
        for r in range(len(s1), len(s2)):
            # add new char, then subtract old char
            codes2[ord(s2[r]) - ord('a')] += 1
            codes2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if codes1 == codes2:
                return True

        return False 