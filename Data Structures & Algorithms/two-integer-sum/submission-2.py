class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize hashmap
        seen = {}

        # iterate over the index and num of array
        for i, n in enumerate(nums):

            # calculate component 
            comp = target - n

            if comp in seen:
                return[seen[comp], i]

            # populate hashmap
            seen[n] = i
        
            

        