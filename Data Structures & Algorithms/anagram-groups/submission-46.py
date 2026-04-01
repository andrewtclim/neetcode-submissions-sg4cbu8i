class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize hashmap {key=char_count, val=[list associated anagrams]}
        res = {}

        for word in strs:
            # create sorted key for each word
            sorted_word = "".join(sorted(word))

            # initalize sorted_word key with empty lists
            if sorted_word not in res:
                res[sorted_word] = []
            
            # append associated word with each sorted_word key
            res[sorted_word].append(word)
        
        return list(res.values())
