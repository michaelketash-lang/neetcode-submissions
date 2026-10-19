class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i , val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                v , j = stack.pop()
                res[j] = i - j
            
            stack.append((val , i))
        
        return res


                