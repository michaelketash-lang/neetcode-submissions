class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        inter = sorted(intervals , key = lambda x : x[0])
        res =[]
        res.append(inter[0])
        for i in range(len(inter)):
            prevEnd = res[-1][1]
            start , end = inter[i]

            if start <= prevEnd:
                res[-1][1] = max(end , prevEnd)
            else:
                res.append(inter[i])
        
        return res