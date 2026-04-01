class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize hashset 
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        # no duplicates detected
        return False