class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        res =[]
        for num in nums:
            heapq.heappush(heap,num)

        for _ in range(len(nums)):
            res.append(heapq.heappop(heap))
        
        return res