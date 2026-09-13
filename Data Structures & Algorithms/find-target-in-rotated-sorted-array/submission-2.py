class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1

        while l <= r:
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] > nums[r]: #left is sorted
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            else: # which means nums[mid] <= nums[r]
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

        