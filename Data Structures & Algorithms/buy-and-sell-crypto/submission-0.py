class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 #initialize max
        l,r = 0,1 #two pointers one prev one cur
        while r < len(prices): #make sure not to exceed
            if prices[l] < prices[r]: #if i am buying less then selling
                profit = prices[r] - prices[l] #calculate profit
                maxP = max(profit,maxP) #take the max
            else:
                l = r
            r += 1
        return maxP