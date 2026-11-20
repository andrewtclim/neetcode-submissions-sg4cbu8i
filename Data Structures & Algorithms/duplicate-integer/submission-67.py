class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # init a hashset (check membership of numbers)
        hashset = set()

        for n in nums:
            # check duplicate
            if n in hashset:
                return True
            hashset.add(n)
        
        return False