class Solution:

    # encode words as one long string following pattern
    # "4#neet4#code" which is "length + delimiter + word"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
        
    def decode(self, s: str) -> List[str]:
        # init result array and pointer for current position
        res = []
        i = 0
    
        while i < len(s):
            # j = delimiter position 
            j = i 
            # move j to the delimiter 
            while s[j] != "#":
                j += 1
            # isolate the length of the word 
            length = int(s[i:j])
            # append the word into res 
            res.append(s[j+1:j+1+length])
            # update i pointer
            i = j+1+length 
        
        return res
