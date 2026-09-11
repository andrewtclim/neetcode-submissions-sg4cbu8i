class Solution:

    # encode as a string 
    # input: ["neet", "code"] -> "4#neet4#code"
    # essentially the len_of_word+delimiter+word repeat 
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        # init res arr and i for current index (starts at next length)
        res = []
        i = 0

        # iter over encoded str
        # j = delimiter position 
        while i < len(s):
            # set j to i 
            j = i 
            # move j to delimiter 
            while s[j] != "#":
                j += 1
            # isolate word length 
            length = int(s[i:j])
            # isolate the next word (j+1 is the start of the word)
            word = s[j+1:j+1+length]
            # append word to arr
            res.append(word)
            # update i pointer to next length position 
            i = j+1+length 

        return res 

