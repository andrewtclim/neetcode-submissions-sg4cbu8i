class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # NOTE: Monotonically decreasing stack that holds (temp, index) tuple pairs 

        # init stack and result array 
        stack = []
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # found a higher temp -> process the days waiting 
            # stack[-1] is the last waiting day and [0] accesses its temp
            while stack and stack[-1][0] < t:
                # process and append the wait time 
                waitTemp, waitIndex = stack.pop()
                waitTime = i - waitIndex
                res[waitIndex] = waitTime
            # otherwise, colder temps get added to stack to wait 
            stack.append((t, i))
        
        return res



        