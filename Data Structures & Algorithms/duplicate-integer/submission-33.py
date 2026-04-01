class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize a set 
        hashset = set()

        # iterate over the array
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False
         