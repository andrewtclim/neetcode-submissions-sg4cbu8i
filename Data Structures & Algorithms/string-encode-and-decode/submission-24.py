class Solution:

    # encode the list of strs into a long string following format
    # length_of_word + delimiter + word
    # since len of word is an invariable length -> splice it so that it is easy to isolate 

    # "4#neet4#code"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    # from the encoded string append each word into the list
    def decode(self, s: str) -> List[str]:
        # init a return array for each word 
        # init a pointer that sits at the beginning of encoded sequence
        res = []
        i = 0

        # iter over words 
        # NOTE: j is the pointer that moves to delimiter
        while i < len(s):
            # move j to the start of encode sequence 
            j = i 
            # move j to #
            while s[j] != "#":
                j += 1
            # isolate length 
            length = int(s[i:j])
            # append the correct word to res array 
            res.append(s[j+1:j+1+length])
            # update i to the next encoded sequence 
            i = j+1+length 
        
        return res

