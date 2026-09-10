class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l , r = 0,0 #starting window indx
        while r < len(nums) - 1:
            far = 0
            # run on the window and check which one take me farthest
            for i in range(l, r + 1):
                far = max(far,nums[i]+i)
            # update new window according to farthest
            l = r + 1
            r = far
            res += 1
        return res

        