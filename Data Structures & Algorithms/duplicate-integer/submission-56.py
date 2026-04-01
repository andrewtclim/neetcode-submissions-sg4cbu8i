class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize a set 
        hashSet = set()

        # iterate through elems -> see a duplicate return True
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        
        # duplicate was not found 
        return False