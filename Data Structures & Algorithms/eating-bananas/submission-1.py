import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_hours(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours <= h
        
        l = 1
        r = max(piles)
        while l < r:
            k = (r+l)// 2
            if calculate_hours(k):
                r = k
            else:
                l = k + 1
        return r
            
            
        