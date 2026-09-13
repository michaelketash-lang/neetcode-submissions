class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # approach: Binary search
        l , r = 0 , len(nums)
        
        while l < r:
            mid = (r + l) // 2 #another way to avoid integer overflow is l + (r-l)//2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
            