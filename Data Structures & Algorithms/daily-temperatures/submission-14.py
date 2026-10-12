class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # monotonicaly decreasing stack 
        stack = [] # (temp, index)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # found a warmer day (process all colder days from top of stack)
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # update our stack with new entry
            stack.append((t, i))
        
        return res