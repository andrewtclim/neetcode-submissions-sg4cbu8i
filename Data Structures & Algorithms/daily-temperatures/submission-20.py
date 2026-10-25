class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init stack 
        stack = [] # (temp, index)
        res = [0]*len(temps)

        for i, t in enumerate(temps):
            while stack and t > stack[-1][0]:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # colder days get appended to top of stack 
            stack.append((t, i))
        
        return res