class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair: pair[0])
        stack = []

        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                start, end = stack.pop()
                stack.append([min(start, interval[0]), max(end, interval[1])])
            else:
                stack.append(interval)
            
        return stack
