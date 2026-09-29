class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # use monotonically decreasing stack (top of stack is last cold day waiting to be processed)
        # init a res array same len of temps
        stack = [] # (temp, index)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # found warm day -> keep processing all colder days 
            # last cold temp < current temp
            while stack and stack[-1][0] < t:
                # isolate the waiting index and temp
                waitTemp, waitIndex = stack.pop()
                # calc and append waiting times to res 
                res[waitIndex] = i - waitIndex
            # add day to the stack 
            stack.append((t, i))
        
        return res 