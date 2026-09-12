class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #starting from the start and from the end
        l,r = 0 , len(heights)-1
        maxi = 0


        #each iteration take the min value between right and left.
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