class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize count map (keys = num, value = freq of num)
        count_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        # populate count map
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # populate freq_list (i = freq of num, elem = [nums w/ that freq])
        for num, freq in count_map.items():
            freq_list[freq].append(num)
        
        # return the last k elements (work backwards from freq_list)
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            # iterate through each bucket
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
        