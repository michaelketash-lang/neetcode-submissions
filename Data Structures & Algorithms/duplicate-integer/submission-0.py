class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        remove_duplicates= set(nums)
        return len(nums) > len(remove_duplicates)
        