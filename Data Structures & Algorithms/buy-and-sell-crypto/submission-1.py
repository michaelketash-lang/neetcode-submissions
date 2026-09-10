class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxP = 0
        i = 0
        for j in range(len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxP = max(profit,maxP)
            else:
                i = j
        return maxP
