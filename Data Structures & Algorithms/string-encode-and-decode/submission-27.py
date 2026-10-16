class Solution:

    # "4#Neet4#Code"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # current pointer (always starts at length (start encoded word))

        while i < len(s):
            j = i # pointer for delimiter
            # move j to the delimiter
            while s[j] != "#":
                j += 1
            
            # isolate the length 
            length = int(s[i:j])

            # isolate the word and append it
            word = s[j+1:j+1+length]
            res.append(word)

            i = j+1+length
        
        return res
 