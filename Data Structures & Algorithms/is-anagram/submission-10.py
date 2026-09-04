class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using zip() and all()
        # ensure same length 
        if len(s) != len(t):
            return False

        # init a char counter list for chars in the english alphabet
        count = [0] * 26

        # iter over chars in cs and ct 
        for cs, ct in zip(s, t):
            # chars in string_s count as +1
            count[ord(cs) - ord('a')] += 1
            # chars in string_t count as -1
            count[ord(ct) - ord('a')] -= 1
        
        # if count in neutralized (all 0's) then the chars appear at same freq 
        # all(iterable) returns True if all the elems in iterable is Truthy 
        return all(c == 0 for c in count)
