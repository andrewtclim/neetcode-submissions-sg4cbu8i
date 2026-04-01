class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize bucket sort array and count_map
        # freq_list (index = freq and elems = [nums w/ freq])
        # count_map {num -> freq}
        freq_list = [[] for i in range(len(nums)+1)]
        count_map = {}

        # populate hashmap
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1

        # populate buckets
        for num, freq in count_map.items():
            freq_list[freq].append(num)
        
        # return last k-elements
        # iterate from right of buckets (least freq <- most freq)
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            # access each bucket
            for num in freq_list[i]:
                res.append(num)
                # check for k - items
                if len(res) == k:
                    return res
        