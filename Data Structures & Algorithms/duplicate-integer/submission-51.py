class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize a hashset
        hashset = set()

        for num in nums:
            # found duplicate
            if num in hashset:
                return True
            hashset.add(num)
        
        return False
         