class Solution:
    def trap(self, height: List[int]) -> int:
        # if height list empty
        if not height:
            return 0
        # two pointers left and right
        l , r = 0 , len(height)-1
        res = 0 # initialize res of water
        max_left = height[l] #take the left most wall
        max_right = height[r] # take the right most wall
        while l < r:
            #if max_left is smaller we can sum until this wall from the left
            if max_left < max_right: 
                l += 1
                max_left = max(max_left,height[l])
                res += max_left - height[l]
            #if max_right is smaller we can sum until this wall from the right
            else:
                r -= 1
                max_right = max(max_right,height[r]) #update max_right
                res += max_right - height[r]
        return res
