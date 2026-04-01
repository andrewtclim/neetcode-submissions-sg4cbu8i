class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        # populate count_map
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # populate freq_list (i = freq and freq_list[i] = nums w/ freq)
        for num, freq in count_map.items():
            freq_list[freq].append(num)

        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res 
         