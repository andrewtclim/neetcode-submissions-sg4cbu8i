class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        for n, freq in count_map.items():
            freq_list[freq].append(n)
        
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res
        