class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True) # Find the first occurrence (start)
        right = self.binarySearch(nums, target, False) # Find the last occurrence (end)
        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1 # Store the index of the found target (-1 if not found)
        
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1 # Target is in the right half
            elif target < nums[m]:
                r = m - 1 # Target is in the left half
            else:
                i = m # Potential answer found, update index
                
                # The 'Bias' logic handles duplicates:
                if leftBias:
                    r = m - 1 # Keep searching to the LEFT for the first occurrence
                else:
                    l = m + 1 # Keep searching to the RIGHT for the last occurrence
                    
        return i
