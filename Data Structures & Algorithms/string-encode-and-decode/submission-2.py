class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res 

    def decode(self, s: str) -> List[str]:
        # initalize pointer for current position (lands on length) and res list
        res, i = [], 0 

        # iterate until the end of our string s 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # when j finds the delimiter #
            length = int(s[i:j])
            
            # append from first letter (j+1) to the last letter (j+1+length) right exclusive
            res.append(s[j+1:j+1+length])

            # update i (current position) to the next length
            i = j + 1 + length 
        
        return res

