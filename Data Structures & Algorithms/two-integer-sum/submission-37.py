class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize hashmap {key=num : val=index}
        seen = {}

        for i, n in enumerate(nums):
            # calculate the complement
            comp = target - n 
            if comp in seen:
                # return complements index and current index
                return [seen[comp], i]
            # populate hashmap with number and it's index
            seen[n] = i 
        
