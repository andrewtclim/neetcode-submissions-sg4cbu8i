class Solution:
    # encoded string: 4#Neet3#Code
    def encode(self, strs: List[str]) -> str:
        result = ''
        for word in strs:
            result += str(len(word)) + '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        # initalize current position and result list
        i, res = 0, []

        while i < len(s):
            # j represents the position of "#"
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            # ends at the next number (indicating length)
            i = j+1+length
        return res

