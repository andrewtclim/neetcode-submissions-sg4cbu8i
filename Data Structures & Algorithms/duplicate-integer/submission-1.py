class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize a hashset
        seen = set()

        # iterate over elems in nums
        for num in nums:
            # if this num was already added in our hashset, we have a duplicate
            if num in seen:
                return True
            # populate our hashset
            seen.add(num)
        
        # if there is no duplicate
        return False

         