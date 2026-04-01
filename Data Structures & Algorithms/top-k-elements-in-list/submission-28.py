class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize bucket sort list [index (freq) -> [nums w/ freq]]
        freq_list = [[] for i in range(len(nums) + 1)]

        # create count map [num -> freq]
        freq_map = Counter(nums)

        for num, freq in freq_map.items():
            freq_list[freq].append(num)
        
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res
        