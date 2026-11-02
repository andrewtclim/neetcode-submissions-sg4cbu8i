class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init stack (monotonically decreasing) and res
        stack = [] # (temp, index)
        res = [0]*len(temps)

        for i, t in enumerate(temps):
            # found a new warmer temp, process all colder temps
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # add new temps to stack 
            stack.append((t, i))
        
        return res