class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        inter = sorted(intervals , key = lambda x : x[0])

        prevEnd = inter[0][1]
        res = 0

        for i in range(1 , len(inter)):
            start , end = inter[i]

            if start >= prevEnd:
                prevEnd = end
            
            else:
                res += 1
                prevEnd = min(prevEnd , end)
        
        return res