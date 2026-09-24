class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # monotonic decreasing stack 
        res = [0] * len(temps)
        stack = [] # tuples of (temp, index)

        for i, t in enumerate(temps):
            # found hotter temp -> process wait times
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                # calc num of days and update correct day
                res[waitIndex] = i - waitIndex
            # push cold days on top 
            stack.append((t, i))
        
        return res