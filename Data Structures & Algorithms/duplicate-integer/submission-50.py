class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initalize hashset
        hashset = []

        for n in nums:
            if n in hashset:
                return True
            hashset.append(n)

        return False
         