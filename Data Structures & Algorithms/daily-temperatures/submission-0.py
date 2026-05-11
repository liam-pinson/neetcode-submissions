class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            print(i, t)
            print(stack)
            print(res)
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
                print(stackT, stackInd)
                print(res[stackInd])
            stack.append((t, i))
            print()

        return res