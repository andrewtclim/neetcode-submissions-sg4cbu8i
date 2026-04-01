class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize hashmap 
        seen = {} # num -> i 

        # iterate over the index and num in list 
        for i, n in enumerate(nums):
            complement = target - n 
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i 
            
        