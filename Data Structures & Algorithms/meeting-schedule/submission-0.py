"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals , key = lambda x : x.start)

        for i in range(1 , len(sorted_intervals)):

            interval1 = sorted_intervals[i - 1]
            interval2 = sorted_intervals[i]

            if interval1.end > interval2.start:
                return False
        
        return True
