# group anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize result hashmap
        result = {}
        
        for word in strs:
            
            # generate a char_count key for each word
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            count_key = tuple(count)
            
            # initalize hashmap with empty lists (if the sequence has not been seen)
            if count_key not in result:
                result[count_key] = []
            
            # populate hashmap with associated anagrams
            result[count_key].append(word)
            
        # return the values(grouped anagrams) in a list
        return list(result.values())