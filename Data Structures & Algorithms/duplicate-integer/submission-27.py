class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize hashset, hashsets can only have unique values
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        
        return False
