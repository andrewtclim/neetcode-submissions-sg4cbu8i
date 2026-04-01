class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize two data structures
        # 1. a hashmap for number count {num -> freq}
        # 2. bucket sort array [i=freq and elem=[nums of that freq]]
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums)+1)] # the last index (max freq) is the amount of nums in input

        # populate hashmap
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # populate buckets 
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)

        # return the last k-elems from the rightside(most frequent) buckets
        res = []
        
        # per bucket
        for i in range(len(freq_buckets)-1, 0, -1):
            # per num in bucket
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        # always append to res first and then have a case where u can return res
        # this makes sure that you are able to return res ex_text_case) nums=[7,7], k=1 