class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize a hashset 
        hashset = set()

        # iterate over numbers in array
        for num in nums:
            # duplicate found in hashset -> True
            if num in hashset:
                return True
            hashset.add(num)
        
        return False