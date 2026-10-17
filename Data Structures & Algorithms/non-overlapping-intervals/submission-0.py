class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        inter_sorted = sorted(intervals , key = lambda x : x[0])
        res = 0
        prevEnd = inter_sorted[0][1]

        for i in range(1 , len(intervals)):
            start , end = inter_sorted[i]
            if start >= prevEnd:
                prevEnd = end
            
            else:
                res += 1
                prevEnd = min(end , prevEnd)
        
        return res