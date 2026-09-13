class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles) # the biggest amount of bananas
        l , r = 1 , maxi

        res = r # h >= len(piles)
        while l <= r:
            k = (r + l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/ k)
            
            if hours > h:
                l = k + 1
            
            else:
                res = min(res, k)
                r = k - 1
        
        return res
        