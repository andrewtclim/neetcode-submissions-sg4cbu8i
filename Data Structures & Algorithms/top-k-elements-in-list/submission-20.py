class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort freq_list where i = frequency and elem = [nums with that freq]
        count_map = {}
        freq_list = [[] for i in range(len(nums)+1)]

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        for num, freq in count_map.items():
            freq_list[freq].append(num)
        
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
         