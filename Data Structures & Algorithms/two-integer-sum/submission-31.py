class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize hashmap [num -> index]
        seen = {}

        for i , n in enumerate(nums):
            comp = target - n 
            if comp in seen:
                # return complements index and current index
                # since nums[comp_index] + nums[curr_index] = target
                return [seen[comp], i]
            seen[n] = i
        
        return -1