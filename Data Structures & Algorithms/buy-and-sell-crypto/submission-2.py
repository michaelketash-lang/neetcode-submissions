class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for right in range(len(prices)):
            if prices[right] > prices[l]:
                profit = max(profit,prices[right] - prices[l])
            
            else:
                l = right
        return profit
        