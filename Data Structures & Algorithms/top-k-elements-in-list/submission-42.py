class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize hashmap {key=num, val=freq of num}
        count_map = {}
        # initalize buckets [i=freq, val=[nums of freq]]
        freq_buckets = [[] for i in range(len(nums) + 1)]

        # populate hashmap 
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # populate buckets
        for num, freq in count_map.items():
            freq_buckets[freq].append(num)
        
        # iterate from the rightmost(most frequent) bucket
        res = []
        for i in range(len(freq_buckets)-1, 0, -1):
            # iterate over nums in bucket
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
