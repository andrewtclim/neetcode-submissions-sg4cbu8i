class Solution:

    # example : "4#neet4#code4#love3#you"
    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, string: str) -> List[str]:
        res, i = [], 0
        
        while i < len(string):
            j = i
            while string[j] != '#':
                j += 1
            length = int(string[i:j])
            res.append(string[j+1:j+1+length])
            i = j + 1 + length
        
        return res