class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_last = {}

        for i , c in enumerate(s):
            char_to_last[c] = i
        
        res , size ,end = [] , 0 ,0

        for i,c in enumerate(s):
            size += 1
            end = max(end , char_to_last[c])

            if end == i:
                res.append(size)
                size = 0
            
        
        return res