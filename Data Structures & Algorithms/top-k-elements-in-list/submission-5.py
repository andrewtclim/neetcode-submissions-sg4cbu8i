class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize hashmap and frequency list
        count_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        # populate count map 
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        # populate freq_list (i = freq and elems = [num of freq])
        for num, freq in count_map.items():
            freq_list[freq].append(num)
        
        # find the last k-elements 
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            # check each freq bucket
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        