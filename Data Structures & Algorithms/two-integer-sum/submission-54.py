class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init a hashmap 
        # {num : index}
        # for each num in nums, calc the complement (if we've seen the comp in our hashmap
        # then return the comp's index and current index)

        seen = {}

        for i, n in enumerate(nums):
            # calc comp
            comp = target - n 
            # checking if it is in the hashmap
            if comp in seen:
                return [seen[comp], i]
            # updating the hashmap
            seen[n] = i
        
        