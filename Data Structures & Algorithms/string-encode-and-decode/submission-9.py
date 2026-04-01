class Solution:

    # each encoded message looks like # 4#neet4#code 
    # so it follows len(word) + '#' + word
    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        # initalize return list and current position pointer
        res, i = [], 0

        while i < len(s):
            # j represents the delimiter position 
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # here j+1 is the first letter
            res.append(s[j+1:j+1+length])
            # position is updated to the next length
            i = j + 1 + length
        return res

