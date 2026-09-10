import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_hours(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h
        
        l = 1
        r = max(piles)
        while l < r:
            mid = (l+r)//2
            if calculate_hours(mid):
                r = mid
            else:
                l = mid + 1
        return r
        