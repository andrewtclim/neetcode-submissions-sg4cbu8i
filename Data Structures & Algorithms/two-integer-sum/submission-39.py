class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize hashmap {k=num, v=index}
        seen = {}

        for i, n in enumerate(nums):
            # calculate the complement 
            comp = target - n 
            # if we have seen the complement before 
            # return the pair [complement_index, curr_index]
            if comp in seen:
                return [seen[comp], i]
            # otherwise add our index to hashmap 
            seen[n] = i 
        
        return -1