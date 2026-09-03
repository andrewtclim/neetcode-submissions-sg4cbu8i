class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize a hashset (ensures unique membership)
        hashset = set()

        # iter over the nums
        for num in nums:
            # check if dupe 
            if num in hashset:
                return True
            hashset.add(num)
        
        # if we never saw a dupe
        return False