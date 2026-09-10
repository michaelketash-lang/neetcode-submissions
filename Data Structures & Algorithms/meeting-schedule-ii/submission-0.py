"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #array with start times sorted
        start_array =sorted([interval.start for interval in intervals])
        #array with ending times sorted
        end_array =sorted([interval.end for interval in intervals])
        used_rooms = 0 #initialize how many rooms we use
        s = 0
        e = 0
        # compare between starting times and end times when starting time is smaller,
        #we need another room if not ets increase e ptr in end_array
        while s < len(intervals):
            if start_array[s] < end_array[e]:
                used_rooms += 1
            else:
                e += 1
            s += 1
        return used_rooms
        
