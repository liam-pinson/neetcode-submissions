"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        list_intervals = []
        for interval in intervals:
            list_intervals.append([interval.start, interval.end])
        list_intervals.sort()

        prevEnd = list_intervals[0][1]

        for start, end in list_intervals[1:]:
            if start < prevEnd:
                return False
            prevEnd = end
        
        return True