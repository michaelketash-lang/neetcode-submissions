class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            #if cur sum is bigger then target need to right -= 1
            if cur_sum > target:
                right -= 1
            #if cur sum is lower than target we need to make cur sum bigger so left += 1
            elif cur_sum < target:
                left += 1
            #equals we will retunr true
            else:
                return [left+1,right+1]
        return [-1,-1]