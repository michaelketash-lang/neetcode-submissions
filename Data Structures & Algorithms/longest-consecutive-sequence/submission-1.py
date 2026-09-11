class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in hash_set: #o(1) check
                #we know num is start of a sequence
                leng = 1
                while (num+leng) in hash_set:
                    leng += 1
                longest = max(leng,longest)
        return longest
        