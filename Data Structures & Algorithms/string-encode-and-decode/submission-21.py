class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    # structure: "4#neet4#code"
    # words: 4#neet4
    # index: ij.... 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 

        # iterate over encoded string (i=current pointer)
        # j = delimiter pointer
        while i < len(s):
            # set j to i 
            j = i 
            # move j to the delimiter
            while s[j] != "#":
                j += 1
            # isolate length as int
            length = int(s[i:j])
            # add word to res arr 
            res.append(s[j+1:j+1+length])
            # update i to next length 
            i = j + 1 + length

        return res

        

