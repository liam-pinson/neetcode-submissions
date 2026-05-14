class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for interval in intervals:
            if stack and interval[0] <= stack[-1][1]:
                new_interval = [stack[-1][0], max(interval[1], stack[-1][1])]
                stack.pop()
                stack.append(new_interval)
            else:
                stack.append(interval)
        
        print(stack)
        return stack