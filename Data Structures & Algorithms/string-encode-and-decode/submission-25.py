class Solution:

    # "4#neet4#code"
    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # current pointer starts at the beginning of each encoded seq 

        while i < len(s):
            # j pointer is the pointer for the delimiter
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            # update ith pointer to next start of encoded seq
            i = j+1+length 
        return res

