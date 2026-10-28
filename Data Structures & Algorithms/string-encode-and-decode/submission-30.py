class Solution:

    def encode(self, strs: List[str]) -> str:
        # "4#Neet4#Code"
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # current pointer, sits at the start of encoded sequence
              # ex) "4#Neet4#Code" i goes from the 4 to the next 4 

        while i < len(s):
            # j tracks the delimiter pointer (to easily isolate length)
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            # update i to next start of encoded sequence
            i = j+1+length
        
        return res
