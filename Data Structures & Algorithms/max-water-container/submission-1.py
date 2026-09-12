class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # space Complexity: O(1)
        # approach: two pointers approach

        #starting from the start and from the end with two pointers
        l,r = 0 , len(heights)-1
        maxi = 0

        #each iteration take the min value between right and left.
        # calculate the width between right and left pointers
        # calculate the area
        # cause we want to maximize area we move the pointers accordingly
        while l < r:
            mini = min(heights[l],heights[r])
            width = r - l
            area = mini * width
            maxi = max(maxi,area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return maxi