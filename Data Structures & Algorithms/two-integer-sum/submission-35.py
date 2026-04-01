class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize hashmap {num -> index}
        seen = {}

        for i, n in enumerate(nums):
            # calulate comp
            comp = target - n 
            if comp in seen:
                return [seen[comp], i]
            seen[n] = i
        
        