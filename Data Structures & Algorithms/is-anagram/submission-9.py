class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # built in Counter hashmap char : ocurrence
        return Counter(s) == Counter(t)