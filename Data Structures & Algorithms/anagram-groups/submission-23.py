class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            # create a count key for each word
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            count_key = tuple(count)

            if count_key not in result:
                result[count_key] = []
            
            result[count_key].append(word)
        
        return list(result.values())
        