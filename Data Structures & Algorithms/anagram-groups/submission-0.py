class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initalize a hashmap to store (occurence count) and (respective anagrams)
        result = {}

        for string in strs:
            # initalize count list 
            count = [0] * 26

            # populate count with nletter occurences
            for c in string:
                count[ord(c) - ord('a')] += 1
            
            # convert to tuple to use as a hashmap key
            count_key = tuple(count)

            # populate hashmap with empty lists 
            if count_key not in result:
                result[count_key] = []
            
            # append associated anagrams with each count_key
            result[count_key].append(string)
        
        return list(result.values())