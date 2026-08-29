class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init hashmap {num : index}
        seen = {}

        for i, num in enumerate(nums):
            comp = target - num 
            if comp in seen:
                return [seen[comp], i]
            # populate hashmap with pairs
            seen[num] = i 
        
        return -1