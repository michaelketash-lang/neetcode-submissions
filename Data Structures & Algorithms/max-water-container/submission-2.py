class Solution:
    def maxArea(self, heights: List[int]) -> int:
        [1,7,2,5,4,7,3,6]

        # initialize part A
        left = 0
        right = len(heights) - 1
        amount = 0
        # part B the while loop of the two pointer approach
        while left < right:
            height = min(heights[left],heights[right])
            width = right - left
            amount = max(amount , height * width)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        # part c is making sure we are returning the maximum amount
        return amount