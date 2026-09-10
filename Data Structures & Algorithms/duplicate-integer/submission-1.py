class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # remove_duplicates= set(nums)
        # return len(nums) > len(remove_duplicates)
        
        # we would like to be able for long list and early duplicate
        # to terminate fast and not scan the whole list so:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False