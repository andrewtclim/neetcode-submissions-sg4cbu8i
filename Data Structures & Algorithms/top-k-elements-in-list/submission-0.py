class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # initalize countmap and freq_list(index = frequency and values = list of nums that occur with that frequency)
        count_map = {}
        freq_list = [ [] for i in range(len(nums) + 1)]
        
        # populate hashmap
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # populate freq_list
        for num, freq in count_map.items():
            freq_list[freq].append(num)
        
        # find last k-elements
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res