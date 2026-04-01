class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_map (key = num and values = freq of num)
        # freq_list (bucket sort where i = freq and elems = [nums with that freq])
        count_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        # populate count_map
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # populate freq_list
        for num, freq in count_map.items():
            freq_list[freq].append(num)

        res = []
        for i in range(len(freq_list)-1,0,-1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
         