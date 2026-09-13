import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pile[i] is the #bananas in the ith pile
        # h : #hours we need to eat all the bananas
        maxi = max(piles)
        l , r = 1 , maxi
        res = r
        while l <= r :
            mid = (r + l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h:
                l = mid + 1
            else :
                res = min(res,mid)
                r = mid - 1
        return res
        

