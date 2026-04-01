class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize set 
        numSet = set()

        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        
        return False