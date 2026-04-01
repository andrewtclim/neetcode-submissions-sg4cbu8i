class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize hashset
        hashset = set()

        # iterate through arr
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False
         