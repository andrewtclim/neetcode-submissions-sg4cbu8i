class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize a hashmap (lookup & insertion is O(1))
        # {number : index}
        seen = {}

        # iter over nums 
        for i, num in enumerate(nums):
            # calc the complement 
            comp = target - num 
            # if we've seen the comp already we can return that index and the current index
            if comp in seen:
                return [seen[comp], i]
            # populate our hashmap 
            seen[num] = i
        
        return -1