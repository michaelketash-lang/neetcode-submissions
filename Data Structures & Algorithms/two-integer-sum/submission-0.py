class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {} #val:index

        for i in range(len(nums)):
            diff = target - nums[i] # take the diff between two numbers
            if diff in hashSet: #checks if in keys
                return [hashSet[diff],i] #prev index,curr index
            hashSet[nums[i]] = i #insert to hashmap
        return
        