class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init a hashmap {num : index}
        seen = {}

        for i, n in enumerate(nums):
            # calc the complement
            comp = target - n 
            if comp in seen:
                return [seen[comp], i]
            seen[n] = i 
        
        