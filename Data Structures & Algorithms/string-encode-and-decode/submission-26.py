class Solution:

    # coded string: "4#Neet4#Code"
    # so follows len_word + delimiter + word
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        '''
        i = current pointer and is left at start of coded sequence (len_word)
        j = delimiter pointer (left at #)
        '''
        res = []
        i = 0 

        while i < len(s):
            # set delimiter to start of code sequence then move to #
            j = i 
            while s[j] != '#':
                j += 1
            # isolate length of word 
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            # update the current pointer i 
            i = j+1+length
        
        return res
