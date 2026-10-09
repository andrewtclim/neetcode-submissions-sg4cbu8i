class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # use a monotonically decreasing stack (coldest day on top, warmest day on bottom)
        stack = [] # (temp, index)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # found warmer day -> process add to result
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # colder day -> keep adding to top of stack 
            stack.append((t, i))
        
        return res